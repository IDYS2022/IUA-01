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

아직 다루지 않은 게슈탈트 항목: 대칭(symmetry) · 평행(parallelism) · 초점(focal point). 2차 이후에 단위를 쓰고 이 표에 더한다.

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
