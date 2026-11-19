# 체계 목록 — 잘 알려진 휴리스틱 · 원리 묶음을 IUA 지식에 잇는다

UIUX에서 '상식'으로 불리는 원리 묶음을 항목 하나씩 IUA 단위 번호에 잇는다. 분석할 때 "이 판단은 닐슨 5번(오류 예방)에 기댄다"처럼 근거를 밝히고, 그 항목의 단위를 바로 꺼내 쓰기 위해서다.

- 이 파일이 체계 → 단위 연결의 유일한 원본이다. 단위 파일에는 적지 않는다. 색인(`_index/frameworks.md`)은 도구가 만든다.
- 찾기: `python3 tools/iua.py frame` (체계와 키 목록) · `python3 tools/iua.py frame 닐슨-5` (그 항목의 단위).
- 표의 키는 바꾸지 않는다. 다른 문서와 진단서가 키로 가리킨다.
- 항목 이름은 우리 말, 원어는 출처의 표기 그대로.
- 단위 칸의 첫 번호가 그 항목을 가장 바로 다루는 단위다.

## 닐슨 10 휴리스틱

출처: Nielsen, J. (1994, 2024 검토). 10 Usability Heuristics for User Interface Design. Nielsen Norman Group. nngroup.com/articles/ten-usability-heuristics/ · 확인: 원문 (2026-11-11)

| 키 | 항목 | 원어 | 단위 |
|---|---|---|---|
| 닐슨-1 | 시스템 상태를 보이게 한다 | Visibility of System Status | PR-009 · PR-010 · PR-011 · ST-019 · ST-021 |
| 닐슨-2 | 시스템을 현실 세계에 맞춘다 | Match Between the System and the Real World | PR-023 · PR-030 · FA-009 |
| 닐슨-3 | 사용자에게 통제와 자유를 준다 | User Control and Freedom | PR-014 · PR-033 · ST-023 · ST-027 · ST-020 · PR-024 |
| 닐슨-4 | 일관성과 표준을 지킨다 | Consistency and Standards | PR-018 · PR-008 |
| 닐슨-5 | 오류를 막는다 | Error Prevention | PR-012 · PR-017 · ST-001 · ST-012 · FA-010 |
| 닐슨-6 | 떠올리기보다 알아보게 한다 | Recognition Rather than Recall | PR-001 · FA-001 · ST-001 · ST-038 |
| 닐슨-7 | 유연하고 효율적으로 쓰게 한다 | Flexibility and Efficiency of Use | PR-026 · TN-007 |
| 닐슨-8 | 미적이고 최소한으로 디자인한다 | Aesthetic and Minimalist Design | PR-002 · PR-015 · PR-016 · PR-003 |
| 닐슨-9 | 오류를 알아채고 · 진단하고 · 회복하게 돕는다 | Help Users Recognize, Diagnose, and Recover from Errors | PR-013 · ST-004 · ST-008 |
| 닐슨-10 | 도움말과 문서를 둔다 | Help and Documentation | PR-027 · ST-028 · ST-027 |

## 노먼의 디자인 기본 원리 7

출처: Norman, D. A. (2013). The Design of Everyday Things (Revised and expanded edition). Basic Books. 1장(상호작용의 기본 개념 여섯)과 2장 끝(디자인의 기본 원리 일곱 — 2장이라는 자리는 요약의 배치로 짐작) · 확인: 2차 — 일곱 원리 목록: andrewclark.super.site/product-book-summaries/the-design-of-everyday-things, 1장의 여섯 개념: elvischidera.com/books/2022-design-of-everyday-things.html (2026-11-11 읽음). 어포던스 · 시그니파이어의 구분은 Norman (2008) 원문 확인 (PR-029)

| 키 | 항목 | 원어 | 단위 |
|---|---|---|---|
| 노먼-발견가능성 | 할 수 있는 것을 알아낼 수 있다 | Discoverability | PR-028 · PR-029 |
| 노먼-피드백 | 한 일의 결과가 바로 알려진다 | Feedback | PR-010 · PR-011 · ST-002 · ST-003 |
| 노먼-개념모델 | 시스템이 어떻게 움직이는지 그려진다 | Conceptual model | PR-031 · FA-015 |
| 노먼-어포던스 | 사물과 사람 사이에 가능한 행동 | Affordances | FA-014 · ST-031 |
| 노먼-시그니파이어 | 어디를 어떻게 다루는지 알리는 신호 | Signifiers | PR-029 · ST-018 · ST-031 |
| 노먼-매핑 | 조작과 결과의 짝이 자연스럽다 | Mappings | PR-030 |
| 노먼-제약 | 할 수 있는 행동을 좁혀 틀릴 길을 줄인다 | Constraints | PR-012 · ST-009 · ST-001 |

## 슈나이더만 8대 황금률

출처: Shneiderman, B., Plaisant, C., Cohen, M., Jacobs, S., & Elmqvist, N. (2016). Designing the User Interface (6th ed.). Pearson. 3.3.4절. cs.umd.edu/users/ben/goldenrules.html · 확인: 원문 (2026-11-11) · 저자 표기는 이 페이지를 따랐다

| 키 | 항목 | 원어 | 단위 |
|---|---|---|---|
| 슈나이더만-1 | 일관성을 지킨다 | Strive for consistency | PR-018 · PR-008 |
| 슈나이더만-2 | 누구나 쓸 수 있게 한다 | Seek universal usability | PR-025 · PR-019 · PR-020 · PR-026 |
| 슈나이더만-3 | 정보가 되는 피드백을 준다 | Offer informative feedback | PR-010 · PR-011 |
| 슈나이더만-4 | 대화가 끝맺음에 이르게 한다 | Design dialogs to yield closure | PR-032 · ST-003 |
| 슈나이더만-5 | 오류를 막는다 | Prevent errors | PR-012 · PR-013 |
| 슈나이더만-6 | 쉽게 되돌리게 한다 | Permit easy reversal of actions | PR-014 |
| 슈나이더만-7 | 사용자가 주도하게 한다 | Keep users in control | PR-033 · ST-026 · PR-024 |
| 슈나이더만-8 | 단기 기억 부담을 줄인다 | Reduce short-term memory load | PR-001 · FA-003 · PR-009 · PR-021 |

## 게슈탈트 묶음 지각

출처: Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt II. Psychologische Forschung, 4, 301–350 · Palmer, S. E. (1992). Common region. Cognitive Psychology, 24(3), 436–447 · Palmer, S. E., & Rock, I. (1994). Rethinking perceptual organization. Psychonomic Bulletin & Review, 1(1), 29–55 · 확인: 2차

| 키 | 항목 | 원어 | 단위 |
|---|---|---|---|
| 게슈탈트-근접 | 가까운 것은 한 묶음으로 보인다 | Proximity | FA-004 · PR-004 |
| 게슈탈트-유사 | 닮은 것은 한 묶음으로 보인다 | Similarity | FA-004 · PR-018 |
| 게슈탈트-공통영역 | 같은 테두리 안의 것은 한 묶음으로 보인다 | Common region | FA-004 · PR-004 |
| 게슈탈트-연결 | 이어진 것은 한 묶음으로 보인다 | Uniform connectedness | FA-004 |
| 게슈탈트-연속 | 매끄럽게 이어지는 선을 따라 읽는다 | Continuity | FA-017 |
| 게슈탈트-폐합 | 빠진 곳을 메워 온전한 모양으로 본다 | Closure | FA-017 |
| 게슈탈트-간결 | 가장 단순한 해석으로 본다 | Prägnanz | FA-017 |
| 게슈탈트-전경배경 | 앞에 선 것과 뒤에 깔린 것을 가른다 | Figure–ground | FA-016 · PR-006 |
| 게슈탈트-공동운명 | 함께 움직이는 것은 한 묶음으로 보인다 | Common fate | FA-018 |

아직 다루지 않은 게슈탈트 항목: 대칭(symmetry) · 평행(parallelism) · 초점(focal point). 단위를 쓰면 이 표에 더한다.

## 평가 방법

화면을 놓고 하는 평가 방법. 렌즈(LN) 단위가 순서를 맡는다.

출처: 각 렌즈 단위의 출처 절 (휴리스틱 평가 · 심각도는 Nielsen, 인지적 워크스루는 Wharton 외) · 확인: 단위마다 다름

| 키 | 항목 | 원어 | 단위 |
|---|---|---|---|
| 평가-휴리스틱평가 | 휴리스틱으로 화면을 훑고 어김마다 심각도를 매긴다 | Heuristic evaluation · Severity ratings | LN-013 · LN-009 |
| 평가-인지적워크스루 | 처음 쓰는 사람의 눈으로 한 걸음씩 따라간다 | Cognitive walkthrough | LN-014 |
| 평가-노먼렌즈 | 노먼 원리 7로 화면을 본다 | — | LN-010 |
| 평가-슈나이더만렌즈 | 8대 황금률로 화면을 본다 | — | LN-011 |
| 평가-게슈탈트렌즈 | 묶음 지각으로 화면의 덩어리를 본다 | — | LN-012 |
| 평가-생성AI렌즈 | 생성형 AI 화면을 겪는 순서로 보고, 지침 18과 원칙 6으로 훑는다 | — | LN-015 |
| 평가-법칙렌즈 | UX 법칙 30을 일곱 묶음으로 화면에 대 본다 | — | LN-016 |

## UX 법칙 30

사람이 보고 · 기억하고 · 고르고 · 기다리는 방식에 대한 심리학의 발견과, 디자인에서 굳어진 경험 원칙을 한데 모은 묶음. 차례는 원어 가나다순이고 중요도 순이 아니다. 성격이 다른 것이 섞여 있다: 여러 번 잰 사실, 조건이 붙는 실험 결과, 측정이 아닌 주장과 원칙. 그래서 항목마다 이어진 단위의 근거 등급을 보고 말한다 (LN-016 '법칙은 근거의 세기가 고르지 않다').

출처: Yablonski, J. (누리집, 2026-11 기준 30개). Laws of UX. lawsofux.com · 같은 이름의 책이 2판까지 나왔다 · 확인: 원문 (2026-11-18) — 사이트에서 30개의 이름과 한 줄 뜻, 이 차수에서 다룬 18개 항목의 쪽(권고 · 내력)을 열어 확인. 책 본문은 읽지 않았다. 항목 이름은 우리 말로 옮겼다

| 키 | 항목 | 원어 | 단위 |
|---|---|---|---|
| 법칙-심미사용성 | 보기 좋으면 쓰기 쉽다고 느낀다 | Aesthetic-Usability Effect | FA-024 |
| 법칙-선택과부하 | 고를 것이 많으면 버거워한다 | Choice Overload | FA-030 · PR-002 |
| 법칙-덩어리 | 낱낱을 뜻 있는 덩어리로 묶는다 | Chunking | FA-003 · PR-004 |
| 법칙-인지편향 | 판단이 한쪽으로 치우친다 | Cognitive Bias | FA-011 · FA-012 · FA-021 · FA-024 · FA-025 |
| 법칙-인지부하 | 화면을 쓰는 데 머리의 품이 든다 | Cognitive Load | FA-022 · PR-015 · PR-002 |
| 법칙-도허티 | 서로 기다리지 않는 빠르기에서 일이 빨라진다 | Doherty Threshold | FA-008 · PR-010 |
| 법칙-피츠 | 멀고 작은 목표는 누르는 데 오래 걸린다 | Fitts's Law | FA-005 · PR-007 · PR-020 |
| 법칙-몰입 | 하는 일에 온전히 빠져든다 | Flow |  |
| 법칙-목표경사 | 끝이 가까울수록 더 힘을 낸다 | Goal-Gradient Effect | FA-027 · PR-032 |
| 법칙-힉 | 고를 것이 늘면 고르는 시간이 는다 | Hick's Law | FA-002 · PR-002 |
| 법칙-야콥 | 다른 데서 배운 방식을 기대한다 | Jakob's Law | FA-009 · PR-008 |
| 법칙-공통영역 | 같은 테두리 안의 것은 한 묶음으로 보인다 | Law of Common Region | FA-004 · PR-004 |
| 법칙-근접 | 가까운 것은 한 묶음으로 보인다 | Law of Proximity | FA-004 · PR-004 |
| 법칙-간결 | 가장 단순한 해석으로 본다 | Law of Prägnanz | FA-017 |
| 법칙-유사 | 닮은 것은 한 묶음으로 보인다 | Law of Similarity | FA-004 · PR-018 |
| 법칙-연결 | 이어진 것은 한 묶음으로 보인다 | Law of Uniform Connectedness | FA-004 |
| 법칙-멘탈모델 | 시스템이 어떻게 움직이는지 머릿속 모형을 만든다 | Mental Model | FA-015 · PR-031 |
| 법칙-밀러 | 한 번에 들고 있을 수 있는 것은 몇 개뿐이다 | Miller's Law | FA-003 |
| 법칙-오컴 | 같은 값이면 가정이 적은 쪽을 고른다 | Occam's Razor |  |
| 법칙-능동적사용자 | 설명을 읽지 않고 바로 써 본다 | Paradox of the Active User | FA-031 · PR-027 |
| 법칙-파레토 | 결과의 대부분이 원인의 일부에서 나온다 | Pareto Principle |  |
| 법칙-파킨슨 | 일은 주어진 시간만큼 늘어난다 | Parkinson's Law |  |
| 법칙-피크엔드 | 가장 센 순간과 끝으로 기억한다 | Peak-End Rule | FA-025 · PR-032 |
| 법칙-포스텔 | 받는 것은 너그럽게, 내보내는 것은 엄격하게 | Postel's Law | PR-042 |
| 법칙-선택주의 | 목표와 닿은 것에만 주의가 간다 | Selective Attention | FA-006 · PR-003 |
| 법칙-계열위치 | 줄지어 본 것은 처음과 끝이 남는다 | Serial Position Effect | FA-026 |
| 법칙-테슬러 | 줄일 수 없는 복잡함은 누군가 맡는다 | Tesler's Law | PR-041 · PR-017 |
| 법칙-폰레스토프 | 여럿 가운데 하나만 다르면 그것이 남는다 | Von Restorff Effect | FA-029 · PR-003 · TN-002 |
| 법칙-작업기억 | 지금 하는 일에 필요한 것을 잠깐 붙든다 | Working Memory | FA-003 · PR-001 · PR-009 |
| 법칙-자이가르닉 | 끝내지 못한 일이 더 잘 기억된다 (다시 셈하니 나타나지 않았다) | Zeigarnik Effect | FA-028 · PR-021 |

단위가 빈 항목: 법칙-몰입 · 법칙-오컴 · 법칙-파레토 · 법칙-파킨슨. 법칙이 말하는 것이 화면의 요구가 아니거나(몰입은 마음의 상태, 오컴은 가설을 고르는 원칙, 파레토는 힘을 쏟을 곳의 어림) 화면 근거를 찾지 못해(파킨슨) 단위를 쓰지 않았다. 가까운 단위가 있어도 법칙을 받치지 않으면 잇지 않는다 (네 항목에 같은 기준). 훑을 때는 '단위 없음'으로 적고, 가까운 단위는 LN-016의 '단위를 쓰지 않은 법칙'을 본다.

법칙 자체의 단위가 아닌 연결: 법칙-인지편향에 이은 다섯은 낱낱의 치우침(잃는 것을 크게 느낌 · 기본값 · 그럴듯한 설명 · 보기 좋음 · 끝과 센 순간)이고 묶음 전체를 다루는 단위는 없다. 법칙-밀러의 원 항목은 7(±2)이라는 수를 적는다. 우리 말로 옮기며 수를 뺐고, 그 수를 화면에 대지 않는 까닭은 FA-003에 있다. 법칙-포스텔과 맞닿는 PR-012(틀리기 어렵게 막는다)는 받치는 단위가 아니라 맞서는 단위라 잇지 않았다 (가르는 조건은 PR-042). 법칙-도허티의 0.4초라는 수는 원 보고서에서 찾지 못했다 (FA-008).

30개 밖이지만 같은 갈래로 쓴 단위: 정보 냄새 FA-023 · PR-040.

## 사람-AI 상호작용 지침 18

AI가 들어간 제품을 놓고 만든 지침. 네 단계로 묶인다: 처음에 · 쓰는 동안 · AI가 틀렸을 때 · 시간이 지나며. 2019년에 나온 것이라 생성하는 화면에만 있는 성질(결과의 달라짐 · 함께 만들기)은 다음 절의 원칙 6으로 메운다.

출처: Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P., Inkpen, K., Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). Guidelines for Human-AI Interaction. CHI 2019. 지침 18개의 이름: Microsoft HAX Design Library, microsoft.com/en-us/haxtoolkit/library/ (네 단계의 이름은 같은 도구 모음의 지침 소개 쪽, haxtoolkit/ai-guidelines/) · 확인: 원문 (2026-11-18) — 이름 18개와 네 단계의 이름, 논문 초록(디자인 실무자 49명이 AI 제품 20개에 대 보았다)을 확인. 항목마다 어느 단계인지는 논문 표를 열지 못해 적지 않았다

| 키 | 항목 | 원어 | 단위 |
|---|---|---|---|
| HAX-1 | 무엇을 할 수 있는지 분명히 한다 | Make clear what the system can do | PR-035 · ST-043 |
| HAX-2 | 얼마나 잘하는지 분명히 한다 | Make clear how well the system can do what it can do | PR-035 · PR-039 |
| HAX-3 | 맥락에 맞는 때에 나선다 | Time services based on context | PR-034 · PR-033 |
| HAX-4 | 맥락에 맞는 정보를 보인다 | Show contextually relevant information | ST-043 |
| HAX-5 | 사회의 관례에 맞춘다 | Match relevant social norms |  |
| HAX-6 | 사회적 치우침을 줄인다 | Mitigate social biases |  |
| HAX-7 | 쉽게 부를 수 있게 한다 | Support efficient invocation | PR-028 · PR-026 |
| HAX-8 | 쉽게 치우거나 무시할 수 있게 한다 | Support efficient dismissal | PR-037 · PR-033 |
| HAX-9 | 쉽게 고칠 수 있게 한다 | Support efficient correction | PR-037 · PR-014 |
| HAX-10 | 확신이 없으면 범위를 좁힌다 | Scope services when in doubt | ST-042 · PR-037 · TN-009 |
| HAX-11 | 왜 그렇게 했는지 분명히 한다 | Make clear why the system did what it did | PR-039 · PR-031 |
| HAX-12 | 최근 상호작용을 기억한다 | Remember recent interactions | PR-037 · PR-038 |
| HAX-13 | 사용자의 행동에서 배운다 | Learn from user behavior |  |
| HAX-14 | 조심스럽게 바꾸고 맞춘다 | Update and adapt cautiously | PR-033 |
| HAX-15 | 잘게 나눈 피드백을 받는다 | Encourage granular feedback | PR-037 |
| HAX-16 | 사용자의 행동이 AI의 앞으로의 동작에 미치는 결과를 알린다 | Convey the consequences of user actions | PR-031 |
| HAX-17 | 전체를 조절할 수 있게 한다 | Provide global controls |  |
| HAX-18 | 바뀐 것을 알린다 | Notify users about changes | PR-035 · PR-034 |

아직 단위가 없는 항목: HAX-5 · HAX-6 · HAX-13 · HAX-17. 사회의 관례와 치우침, 사용자에게 맞춰 가는 개인화, AI가 무엇을 지켜보고 어떻게 움직일지를 전체 설정으로 맞추는 일은 IUA 지식에 아직 없다. 훑을 때는 '단위 없음 · 추론'으로 적는다.

## 생성형 AI 디자인 원칙 6

생성하는 AI에만 있는 성질을 다루는 원칙. 원칙마다 전략 넷이 딸려 모두 24개다. 문헌 검토 → 워크숍과 실무자 의견 → 실무자 18명이 상용 생성형 AI 도구 9개를 평가 → 제품 팀 워크숍 둘을 거쳐 다듬어졌다.

출처: Weisz, J. D., He, J., Muller, M., Hoefer, G., Miles, R., & Geyer, W. (2024). Design Principles for Generative AI Applications. CHI 2024. arxiv.org/abs/2401.14484 · 확인: 원문 (2026-11-18) — 원칙 6개와 전략 24개의 이름, 만든 과정을 확인. 본문 뒤쪽(사례 적용 부분)은 읽지 않았다

| 키 | 항목 | 원어 | 단위 |
|---|---|---|---|
| 생성AI-책임 | 책임 있게 디자인한다 (사람의 필요에서 시작하고, 해를 살핀다) | Design Responsibly | PR-024 |
| 생성AI-달라짐 | 생성의 달라짐에 맞춰 디자인한다 | Design for Generative Variability | PR-038 |
| 생성AI-멘탈모델 | 멘탈 모델에 맞춰 디자인한다 | Design for Mental Models | PR-035 · PR-031 · FA-015 |
| 생성AI-함께만들기 | 함께 만들기에 맞춰 디자인한다 | Design for Co-Creation | PR-036 · PR-037 · ST-043 |
| 생성AI-믿음 | 알맞은 믿음과 기댐에 맞춰 디자인한다 | Design for Appropriate Trust & Reliance | PR-039 · PR-035 · FA-021 · TN-009 |
| 생성AI-불완전함 | 불완전함에 맞춰 디자인한다 | Design for Imperfection | PR-037 · PR-039 |

'생성AI-책임'에 이은 PR-024는 속여 밀지 않는다는 한 면만 받친다. 해를 미리 살피고 지켜보는 일을 다루는 단위는 아직 없다.
