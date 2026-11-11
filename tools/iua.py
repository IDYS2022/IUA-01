# IUA 지식 도구 — 색인 만들기 · 찾기 · 카드 · 검사. 세는 일과 찾는 일은 코드가, 올리는 결정은 사람이.
# 쓰는 법 (저장소 어디서든):
#   python3 tools/iua.py check               양식 · 어휘 · 끊긴 줄 · 한도 · 올릴 후보. 문제가 없으면 한 줄
#   python3 tools/iua.py index               knowledge/_index/ 다시 만들기 (signals · map · tensions)
#   python3 tools/iua.py find <신호> …       신호로 단위 찾기. 한 줄씩, 겹친 신호 많은 순. --type PR 로 종류 제한
#   python3 tools/iua.py card <번호> …       카드만 출력 (강의는 내지 않는다)
# 다른 패키지를 쓰지 않는다 (표준 라이브러리만).
import os, re, sys, collections

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # 저장소 맨 위 (플러그인으로 설치되면 플러그인 폴더)
KN = os.path.join(ROOT, 'knowledge')
INDEX = os.path.join(KN, '_index')

TYPES = {'FA': '사실', 'PR': '원리', 'TN': '긴장', 'ST': '상황', 'CS': '사례', 'LN': '렌즈'}
ORDER = ['LN', 'PR', 'ST', 'TN', 'FA', 'CS']                                # find 출력 순서 = 꺼내는 순서
ROOT_OK = {'FA': set(), 'PR': {'FA'}, 'TN': {'PR'}, 'ST': {'PR', 'TN'}, 'CS': {'ST', 'PR', 'TN'}, 'LN': {'PR', 'TN', 'ST'}}
REQUIRED = ['번호', '종류', '제목', '한 줄', '영역', '신호', '뿌리', '긴장', '근거', '상태', '고친 날']
CARD = {'FA': ['주장', '어떻게 알았나', '디자인에 주는 뜻', '한계'],
        'PR': ['주장', '적용되는 때', '약해지는 때', '요구로 바꾸면', '확인 질문'],
        'TN': ['맞서는 둘', '이기는 조건', '지는 쪽을 살리는 법', '확인 질문'],
        'ST': ['상황', '한다', '하지 않는다', '왜', '확인 질문'],
        'CS': ['맥락', '핵심', '결정', '결과', '배운 것'],
        'LN': ['먼저 볼 것', '보통 지배하는 원리', '자주 틀리는 곳', '되물을 질문']}
GRADES = ['A', 'B', 'C', 'D']
CONFIRM = {'A': ['원문'], 'B': ['원문', '2차']}   # 근거 등급이 요구하는 확인 상태. C · D는 묻지 않는다
STATES = ['초안', '검토됨', '확립', '폐기']
SHELVES = ['사람', '일과 맥락', '정보 구조', '시각 구조', '상호작용', '흐름', '내용과 말', '시간과 움직임',
           '접근성과 포용', '기기와 매체', '신뢰와 윤리', '복잡한 시스템']
MAX_CARD_LINES = 12      # 임시. 시험에서 고친다
MAX_ONE_LINE = 60        # 한 줄 글자 수
SIGNALS_MIN, SIGNALS_MAX = 3, 6
PROMOTE = 3              # 같은 추론이 사례 이 수에서 반복 → 상황 후보 · 초안이 사례 이 수에서 맞음 → 확립 후보
ID_RE = re.compile(r'^(FA|PR|TN|ST|CS|LN)-(\d{3})$')
FILE_RE = re.compile(r'^(FA|PR|TN|ST|CS|LN)-(\d{3})-[a-z0-9-]+\.md$')


# ── 읽기 ──────────────────────────────────────────────────────────────────────

def parse_list(v):
    v = v.strip()
    if v.startswith('[') and v.endswith(']'):
        v = v[1:-1]
    return [x.strip() for x in v.split(',') if x.strip()]


def read_unit(path):
    text = open(path, encoding='utf-8').read()
    u = {'path': path, 'file': os.path.basename(path), 'folder': os.path.basename(os.path.dirname(path)),
         'head': {}, 'card': [], 'card_fields': {}, 'sources': [], 'problems': []}
    m = re.match(r'---\n(.*?)\n---\n(.*)', text, re.S)
    if not m:
        u['problems'].append('머리표(---)가 없다')
        return u
    for line in m[1].split('\n'):
        if ':' not in line or line.startswith('#'):
            continue
        k, v = line.split(':', 1)
        v = v.split('  #')[0].strip()          # 줄 끝 주석은 버린다
        u['head'][k.strip()] = parse_list(v) if k.strip() in ('신호', '뿌리', '긴장') else v
    body = m[2]
    sec = None
    for line in body.split('\n'):
        if line.startswith('## '):
            sec = line[3:].strip()
            sub = None
            continue
        if line.startswith('### '):
            sub = line[4:].strip()
            continue
        s = line.strip()
        if not s:
            continue
        if sec == '카드':
            u['card'].append(s)
            if s.startswith('- ') and ':' in s:
                k, v = s[2:].split(':', 1)
                u['card_fields'][k.strip()] = v.strip()
        elif sec == '강의' and sub == '출처' and s.startswith('- '):
            u['sources'].append(s[2:])
    u['has_card'] = '## 카드' in body
    u['has_lecture'] = '## 강의' in body
    return u


def load_units():
    units = {}
    dup = []
    for t in TYPES:
        d = os.path.join(KN, t)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md'):
                continue
            u = read_unit(os.path.join(d, f))
            uid = u['head'].get('번호') or f[:6]
            if uid in units:
                dup.append(uid)
            units[uid] = u
    return units, dup


def load_vocab():
    """신호 → {갈래, 뜻, 같은 말}. 같은 말 → 신호도 함께 돌려준다."""
    vocab, syn, group = collections.OrderedDict(), {}, None
    path = os.path.join(KN, '_vocab.md')
    for line in open(path, encoding='utf-8'):
        if line.startswith('## '):
            group = line[3:].split('—')[0].strip()
            continue
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 3 or cells[0] in ('신호', '') or set(cells[0]) <= set('-'):
            continue
        name, meaning, same = cells[0], cells[1], cells[2]
        vocab[name] = {'갈래': group, '뜻': meaning, '같은 말': [s.strip() for s in same.split(',') if s.strip()]}
        syn[name] = name
        for s in vocab[name]['같은 말']:
            syn[s] = name
    return vocab, syn


def children_of(units):
    kids = collections.defaultdict(list)
    for uid, u in units.items():
        for r in u['head'].get('뿌리', []):
            kids[r].append(uid)
    return kids


def one_line(u):
    return u['head'].get('한 줄', '').strip()


def kind(uid):
    return uid[:2]


# ── check ─────────────────────────────────────────────────────────────────────

def check():
    units, dup = load_units()
    vocab, _ = load_vocab()
    problems = [f'{d}: 번호 중복' for d in dup]
    for uid, u in units.items():
        p = u['problems']
        h = u['head']
        t = kind(uid)
        if not FILE_RE.match(u['file']):
            p.append('파일 이름이 <기호>-<세 자리>-<영어>.md 꼴이 아니다')
        if not ID_RE.match(uid):
            p.append('번호 꼴이 아니다')
        if u['file'][:6] != uid:
            p.append(f'파일 이름({u["file"][:6]})과 번호가 다르다')
        if u['folder'] != t:
            p.append(f'폴더({u["folder"]})와 기호({t})가 다르다')
        for k in REQUIRED:
            if k not in h:
                p.append(f'머리표에 "{k}" 칸이 없다')
        if h.get('종류') and h['종류'] != TYPES.get(t):
            p.append(f'종류({h["종류"]})가 기호({t} = {TYPES.get(t)})와 다르다')
        if h.get('근거') and h['근거'] not in GRADES:
            p.append(f'근거 등급({h["근거"]})은 A·B·C·D 중 하나')
        if h.get('상태') and h['상태'] not in STATES:
            p.append(f'상태({h["상태"]})는 초안·검토됨·확립·폐기 중 하나')
        if h.get('상태') == '폐기' and not h.get('대신'):
            p.append('폐기인데 "대신: <번호>"가 없다')
        if h.get('영역') and h['영역'] not in SHELVES:
            p.append(f'영역({h["영역"]})이 서가 12곳에 없다')
        if h.get('고친 날') and not re.match(r'^\d{4}-\d{2}-\d{2}$', h['고친 날']):
            p.append('고친 날은 YYYY-MM-DD')
        ol = one_line(u)
        if not ol:
            p.append('한 줄이 비었다')
        elif len(ol) > MAX_ONE_LINE:
            p.append(f'한 줄이 {len(ol)}자 (한도 {MAX_ONE_LINE})')
        sig = h.get('신호', [])
        if not (SIGNALS_MIN <= len(sig) <= SIGNALS_MAX):
            p.append(f'신호가 {len(sig)}개 (기준 {SIGNALS_MIN}~{SIGNALS_MAX})')
        for s in sig:
            if s not in vocab:
                p.append(f'신호 "{s}"가 _vocab.md에 없다')
        roots = h.get('뿌리', [])
        for r in roots:
            if r not in units:
                p.append(f'뿌리 {r}가 없는 번호')
            elif kind(r) not in ROOT_OK[t]:
                p.append(f'{t}의 뿌리로 {kind(r)}({r})는 쓸 수 없다 (가능: {"·".join(sorted(ROOT_OK[t])) or "없음"})')
        if t == 'FA' and roots:
            p.append('사실(FA)은 뿌리를 두지 않는다 (출처가 뿌리)')
        if t in ('PR', 'ST') and not roots:
            p.append('끊긴 줄: 뿌리가 없다')
        if t == 'TN' and not (len(roots) == 2 and all(kind(r) == 'PR' for r in roots)):
            p.append('긴장(TN)의 뿌리는 원리(PR) 정확히 2개')
        for x in h.get('긴장', []):
            if x not in units:
                p.append(f'긴장 {x}가 없는 번호')
            elif kind(x) != 'TN':
                p.append(f'긴장 칸에는 TN만 ({x})')
        if not u['has_card']:
            p.append('"## 카드"가 없다')
        else:
            if len(u['card']) > MAX_CARD_LINES:
                p.append(f'카드가 {len(u["card"])}줄 (한도 {MAX_CARD_LINES})')
            for k in CARD[t]:
                if k not in u['card_fields'] or not u['card_fields'][k]:
                    p.append(f'카드에 "{k}" 칸이 없거나 비었다')
        if h.get('근거') in CONFIRM:
            if h.get('확인') not in CONFIRM[h['근거']]:
                p.append(f'근거 {h["근거"]}는 확인이 {"·".join(CONFIRM[h["근거"]])}여야 한다 (지금: {h.get("확인", "없음")})')
            confirmed = [s for s in u['sources'] if '미확인' not in s]
            if not confirmed:
                p.append(f'근거 {h["근거"]}인데 확인한 출처가 없다 (### 출처에 "- " 줄)')
        if h.get('확인') and h['확인'] not in ('원문', '2차', '미확인'):
            p.append(f'확인({h["확인"]})은 원문 · 2차 · 미확인 중 하나')
        # 부품 이름이 요구에 들어갔나 (IUA는 값을 말하지 않는다)
        for k in ('요구로 바꾸면', '한다', '이뤄져야 할 것'):
            v = u['card_fields'].get(k, '')
            if re.search(r'\b(Button|Select|Dialog|Tabs|Card|Input|Popover|Sheet|Drawer|Carousel|Table)\b', v):
                p.append(f'"{k}" 칸에 부품 이름이 있다. 요구는 "무엇이 이뤄져야 하나"로')
        problems += [f'{uid}: {x}' for x in p]

    # 올릴 후보 — 세는 일만 한다. 올리는 결정은 사람이
    kids = children_of(units)
    hints = []
    for uid, u in units.items():
        cs = [k for k in kids.get(uid, []) if kind(k) == 'CS']
        if kind(uid) == 'ST' and u['head'].get('근거') == 'D' and len(cs) >= PROMOTE:
            hints.append(f'{uid}: 추론(D)이 사례 {len(cs)}건에서 반복 → 근거를 올릴 후보 (사람이 결정)')
        if u['head'].get('상태') == '초안' and len(cs) >= PROMOTE:
            hints.append(f'{uid}: 초안인데 사례 {len(cs)}건이 가리킴 → 확립 후보 (사람이 결정)')
    for line in problems:
        print('문제  ' + line)
    for line in hints:
        print('후보  ' + line)
    if not problems:
        by = collections.Counter(kind(k) for k in units)
        print('문제 없음 · 단위 ' + str(len(units)) + '장 (' + ' · '.join(f'{t} {by.get(t, 0)}' for t in TYPES) + ')')
    return 1 if problems else 0


# ── index ─────────────────────────────────────────────────────────────────────

NOTE = '<!-- 자동 생성: python3 tools/iua.py index — 손으로 고치지 않는다. 원본은 각 단위의 머리표 -->\n'


def fmt(uid, units, extra=''):
    u = units[uid]
    s = f'`{uid}` {u["head"].get("제목", "")} — {one_line(u)}'
    return s + (f' ({extra})' if extra else '')


def index():
    units, _ = load_units()
    vocab, _ = load_vocab()
    os.makedirs(INDEX, exist_ok=True)
    order = {t: i for i, t in enumerate(ORDER)}
    sort_key = lambda k: (order[kind(k)], k)

    # signals.md — 신호 → 단위
    out = [NOTE, '# 신호 색인 — 신호 → 단위 (한 줄)', '', '맥락 카드의 신호로 여기서 찾는다. 같은 신호 안의 순서는 꺼내는 순서(렌즈 → 원리 → 상황 → 긴장 → 사실 → 사례).', '']
    group = None
    for sig, meta in vocab.items():
        if meta['갈래'] != group:
            group = meta['갈래']
            out += [f'## {group}', '']
        hits = sorted([k for k, u in units.items() if sig in u['head'].get('신호', [])], key=sort_key)
        out.append(f'### {sig}' + (f' — {meta["뜻"]}' if meta['뜻'] else ''))
        out += [f'- {fmt(k, units)}' for k in hits] if hits else ['- (아직 없음)']
        out.append('')
    open(os.path.join(INDEX, 'signals.md'), 'w', encoding='utf-8').write('\n'.join(out))

    # map.md — 왜 사슬
    kids = children_of(units)
    out = [NOTE, '# 왜 사슬 — 사실 → 원리 → 상황 → 사례 (렌즈는 가리키는 원리 아래)', '', '아래로 갈수록 구체적이다. 위로 올라가면 "왜"의 답이 나온다.', '']

    def walk(uid, depth, seen):
        pre = '  ' * depth + '- '
        out.append(pre + fmt(uid, units, TYPES[kind(uid)]))
        for k in sorted(kids.get(uid, []), key=sort_key):
            if k in seen:
                out.append('  ' * (depth + 1) + f'- `{k}` (위에 있음)')
                continue
            seen.add(k)
            walk(k, depth + 1, seen)

    seen = set()
    for fa in sorted(k for k in units if kind(k) == 'FA'):
        seen.add(fa)
        walk(fa, 0, seen)
    orphans = [k for k in units if k not in seen and kind(k) != 'TN']
    if orphans:
        out += ['', '## 사슬에 들지 않은 단위 (뿌리가 없거나 끊김)', ''] + [f'- {fmt(k, units, TYPES[kind(k)])}' for k in sorted(orphans)]
    open(os.path.join(INDEX, 'map.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

    # tensions.md — 긴장 표
    out = [NOTE, '# 긴장 표 — 원리 둘이 맞설 때', '', '| 번호 | 맞서는 둘 | 이기는 조건 | 근거 | 상태 |', '|---|---|---|---|---|']
    for tn in sorted(k for k in units if kind(k) == 'TN'):
        u = units[tn]
        pair = ' ↔ '.join(f'`{r}` {units[r]["head"].get("제목", "")}' if r in units else r for r in u['head'].get('뿌리', []))
        out.append(f'| `{tn}` | {pair} | {u["card_fields"].get("이기는 조건", "")} | {u["head"].get("근거", "")} | {u["head"].get("상태", "")} |')
    open(os.path.join(INDEX, 'tensions.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(f'색인 3개 다시 만듦 · 단위 {len(units)}장 · 신호 {len(vocab)}개')


# ── find · card ───────────────────────────────────────────────────────────────

def find(args):
    units, _ = load_units()
    vocab, syn = load_vocab()
    only = None
    if '--type' in args:
        i = args.index('--type')
        only = args[i + 1]
        args = args[:i] + args[i + 2:]
    # 신호는 띄어쓰기를 품을 수 있다 ("복잡해 보임"). 붙여서 긴 말부터 찾는다
    text = ' ' + ' '.join(args).replace(',', ' ') + ' '   # '·'는 신호 이름의 일부일 수 있어 그대로 둔다
    asked = []
    for key in sorted(syn, key=len, reverse=True):
        if key in text:
            asked.append(syn[key])
            text = text.replace(key, ' ')
    unknown = text.split()
    if unknown:
        print('어휘에 없는 말: ' + ', '.join(unknown) + ' (_vocab.md에 더하거나 같은 말로 묶는다)')
    if not asked:
        print('찾을 신호가 없다. 예: find 초심자 입력')
        return
    print('신호: ' + ' · '.join(dict.fromkeys(asked)))
    rows = []
    for uid, u in units.items():
        if only and kind(uid) != only:
            continue
        if u['head'].get('상태') == '폐기':
            continue
        hit = [s for s in u['head'].get('신호', []) if s in asked]
        if hit:
            rows.append((len(hit), uid, hit))
    order = {t: i for i, t in enumerate(ORDER)}
    rows.sort(key=lambda r: (order[kind(r[1])], -r[0], r[1]))
    cur = None
    for n, uid, hit in rows:
        if kind(uid) != cur:
            cur = kind(uid)
            print(f'\n[{TYPES[cur]} {cur}]')
        h = units[uid]['head']
        print(f'  {uid} · {one_line(units[uid])} · 겹침 {n} ({"·".join(hit)}) · 근거 {h.get("근거", "?")} · {h.get("상태", "?")}')
    if not rows:
        print('맞는 단위가 없다. 사실(FA)에서 추론하고 "추론 · D"를 붙인다.')


def card(ids):
    units, _ = load_units()
    for uid in ids:
        u = units.get(uid)
        if not u:
            print(f'{uid}: 없는 번호')
            continue
        h = u['head']
        print(f'# {uid} {h.get("제목", "")}  [{h.get("종류", "")} · {h.get("영역", "")} · 근거 {h.get("근거", "")} · {h.get("상태", "")}]')
        print(f'한 줄: {one_line(u)}')
        print(f'신호: {", ".join(h.get("신호", []))} · 뿌리: {", ".join(h.get("뿌리", [])) or "없음"} · 긴장: {", ".join(h.get("긴장", [])) or "없음"}')
        for line in u['card']:
            print(line)
        print()


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'check':
        sys.exit(check())
    if cmd == 'index':
        index()
    elif cmd == 'find':
        find(sys.argv[2:])
    elif cmd == 'card':
        card(sys.argv[2:])
    else:
        print(__doc__ or open(__file__, encoding='utf-8').read().split('\n\n')[0])


if __name__ == '__main__':
    main()
