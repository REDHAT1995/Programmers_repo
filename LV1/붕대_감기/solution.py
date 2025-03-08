def solution(bandage: list, health: int, attacks: list) -> int:
    """
    붕대 감기 기술을 사용하여 캐릭터가 생존할 수 있는지 확인하는 함수
    
    Args:
        bandage (list): [시전 시간, 초당 회복량, 추가 회복량] 형태의 리스트
        health (int): 캐릭터의 최대 체력
        attacks (list): [[공격 시간, 피해량]] 형태의 2차원 리스트
        
    Returns:
        int: 모든 공격이 끝난 직후 남은 체력 (죽으면 -1)
        
    Examples:
        >>> solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])
        5
    """
    # 입력값 분리 및 초기화
    cast_time, heal_per_sec, bonus_heal = bandage  # 시전 시간, 초당 회복량, 추가 회복량
    max_health = health  # 최대 체력
    current_health = max_health  # 현재 체력을 최대 체력으로 초기화
    continuous_success = 0  # 연속 성공 시간 카운터
    
    # 공격 정보를 시간을 키로 하는 딕셔너리로 변환 (시간 복잡도 개선)
    attack_dict = {time: damage for time, damage in attacks}
    last_attack_time = attacks[-1][0]  # 마지막 공격 시간

    # 1초부터 마지막 공격 시간까지 시뮬레이션
    for current_time in range(1, last_attack_time + 1):
        # 현재 시간에 공격이 있는 경우
        if current_time in attack_dict:
            current_health -= attack_dict[current_time]  # 피해량만큼 체력 감소
            continuous_success = 0  # 연속 성공 시간 초기화
            
            # 체력이 0 이하가 되면 캐릭터 사망
            if current_health <= 0:
                return -1
        # 공격이 없는 경우 (회복 진행)
        else:
            # 기본 회복량 적용
            current_health += heal_per_sec
            continuous_success += 1  # 연속 성공 시간 증가
            
            # 연속 성공 보너스 체크
            if continuous_success == cast_time:
                current_health += bonus_heal  # 추가 회복량 적용
                continuous_success = 0  # 연속 성공 시간 초기화
            
            # 최대 체력 초과 방지
            current_health = min(current_health, max_health)

    # 모든 공격이 끝난 후 남은 체력 반환
    return current_health


# 테스트 케이스
def test_solution():
    """
    solution 함수를 테스트하는 함수
    """
    # 테스트 케이스 1: 기본 케이스
    assert solution(
        [5, 1, 5], 
        30, 
        [[2, 10], [9, 15], [10, 5], [11, 5]]
    ) == 5
    
    # 테스트 케이스 2: 사망 케이스 (체력이 0 이하)
    assert solution(
        [3, 2, 7], 
        20, 
        [[1, 15], [5, 16], [8, 6]]
    ) == -1
    
    # 테스트 케이스 3: 사망 케이스 (다른 시전 시간)
    assert solution(
        [4, 2, 7], 
        20, 
        [[1, 15], [5, 16], [8, 6]]
    ) == -1
    
    # 테스트 케이스 4: 최소 입력값 케이스
    assert solution(
        [1, 1, 1],
        5,
        [[1, 2], [3, 2]]
    ) == 3
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 