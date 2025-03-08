# 붕대 감기

## 문제 설명
게임 캐릭터가 붕대 감기 기술을 사용하여 체력을 회복하는 동안 몬스터의 공격을 받으며 생존할 수 있는지 확인하는 문제입니다.

## 알고리즘 순서도
```mermaid
flowchart TD
    A[시작] --> B[초기화]
    B --> C[공격 정보 변환]
    C --> D[시간 1로 설정]
    D --> E{시간 <= 마지막 공격?}
    E -->|Yes| F{현재 시간이 공격?}
    F -->|Yes| G[피해량 적용]
    G --> H{체력 <= 0?}
    H -->|Yes| I[return -1]
    H -->|No| J[시간 증가]
    F -->|No| K[기본 회복]
    K --> L{연속 성공 = 시전 시간?}
    L -->|Yes| M[추가 회복]
    L -->|No| N[체력 제한]
    M --> N
    N --> J
    J --> E
    E -->|No| O[return 체력]
    O --> P[종료]
    I --> P
```

## 문제 해결 방법
1. 초기 설정
   - 현재 체력을 최대 체력으로 설정
   - 연속 성공 시간을 0으로 초기화
   - 현재 시간을 0으로 설정

2. 시간별 처리
   - 공격 시간인 경우:
     * 공격 데미지 적용
     * 연속 성공 초기화
   - 공격 시간이 아닌 경우:
     * 초당 회복량 적용
     * 연속 성공 시간 증가
     * 시전 시간 달성 시 추가 회복

3. 체력 관리
   - 최대 체력 초과 불가
   - 0 이하면 즉시 종료 (-1 반환)

## 제약 조건
- bandage = [시전 시간, 초당 회복량, 추가 회복량]
  * 1 ≤ 시전 시간 ≤ 50
  * 1 ≤ 초당 회복량 ≤ 100
  * 1 ≤ 추가 회복량 ≤ 100
- 1 ≤ health ≤ 1,000
- 1 ≤ attacks의 길이 ≤ 100
- attacks[i] = [공격 시간, 피해량]
  * 1 ≤ 공격 시간 ≤ 1,000
  * 1 ≤ 피해량 ≤ 100

## 구현 설명
```python
# 초기 설정
current_health = health
continuous_success = 0
current_time = 0

# 시간별 처리
while current_time <= last_attack_time:
    if is_attack_time:
        current_health -= damage
        continuous_success = 0
    else:
        current_health += heal_per_second
        continuous_success += 1
        
        if continuous_success == cast_time:
            current_health += additional_heal
            continuous_success = 0
            
    current_health = min(current_health, health)
```

## 성능 분석
- 시간 복잡도: O(T)
  - T: 마지막 공격 시간
- 공간 복잡도: O(1)
  - 고정된 변수만 사용

## 개선 사항
- 공격 시간 사이의 회복량 한 번에 계산
- 시간 기반 처리를 이벤트 기반으로 변경
- 메모리 사용량 최적화 