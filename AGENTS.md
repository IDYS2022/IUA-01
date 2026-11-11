# AGENTS.md

모든 AI(모델 · 도구 무관)의 입구. 이 파일은 짧게 둔다. 자세한 것은 필요할 때 읽는 문서에 있다.

## IUA가 무엇인가

UIUX 분석만 하는 에이전트. 맥락 카드를 받아 원리로 핵심을 짚고 설계 요구서(그리기 전) · 진단서(그린 뒤)를 낸다. 부품 · 값은 정하지 않는다.

## IUA로 일할 때 (분석을 맡은 AI)

1. `IUA_CORE.md`를 읽는다 (정체 · 꺼내는 순서와 한도).
2. `protocol/README.md`를 읽는다 (받는 카드 · 내는 양식).
3. `python3 tools/iua.py find <신호> …` → `python3 tools/iua.py card <번호> …`. 신호는 `knowledge/_vocab.md`의 말.
4. 양식 그대로 낸다. 파일은 고치지 않는다.

Claude Code에 플러그인으로 설치돼 있으면 같은 일을 에이전트 `iua:iua`가 한다 (`agents/iua.md`).

## IUA를 고칠 때 (유지 관리)

- 지식 단위를 쓰거나 고치기 전에 `knowledge/_format.md`(양식)와 `README.md`의 '운영 규칙'을 읽는다. 전부 읽지 않는다.
- 쓰기 전에 `find`로 같은 주장이 있는지 찾는다. 있으면 그 장을 고친다.
- 저장 전 `python3 tools/iua.py check` → 문제 0. 단위를 더하거나 고쳤으면 `python3 tools/iua.py index`.
- `knowledge/_index/`는 손으로 고치지 않는다.
- 출처는 확인한 것만 적는다. 확인 못 했으면 `출처 미확인`.
- 회사 · 프로덕트 이름을 지식에 넣지 않는다 (출처 절의 발행처 이름은 된다).
- 커밋 메시지에 왜 바꿨는지 쓴다. 플러그인 구조(`.claude-plugin/` · `agents/` · `skills/`)를 바꿨으면 `claude plugin validate .`도 돌린다.
