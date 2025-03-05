from typing import List

def convert_to_minutes(time: int) -> int:
    """
    시간을 분으로 변환합니다.
    """
    return time // 100 * 60 + time % 100

def solution(schedules: List[int], timelogs: List[List[int]], startday: int) -> int:
    """
    상품을 받을 직원의 수를 계산합니다.
    
    Args:
        schedules (List[int]): 직원 n명이 설정한 출근 희망 시각을 담은 1차원 정수 배열
        timelogs (List[List[int]]): 직원들이 일주일 동안 출근한 시각을 담은 2차원 정수 배열
        startday (int): 이벤트를 시작한 요일 (1: 월요일, 2: 화요일, ..., 7: 일요일)
        
    Returns:
        int: 상품을 받을 직원의 수
        
    Raises:
        ValueError: 입력값이 제약 조건을 만족하지 않는 경우
    """
    
    # 입력값 검증
    if not (1 <= len(schedules) <= 1000 and 
            1 <= len(timelogs) <= 1000 and 
            1 <= startday <= 7):
        raise ValueError("Invalid input parameters")
    
    # TODO: 알고리즘 구현
    answer = 0
    for cur_pnum, cur_schedule in enumerate(schedules):
        cur_schedule = convert_to_minutes(cur_schedule) # 분으로 시간을 변경
        
        cur_day = startday  # 이벤트 시작 날짜
        check = True        # 모든 날짜에 출근을 제대로 했는지 체크
        
        cur_timelogs = timelogs[cur_pnum]   # 출근 시간 리스트
        for cur_timelog in cur_timelogs:
            cur_timelog = convert_to_minutes(cur_timelog) # 분으로 시간을 변경
            if (cur_day-1) % 7 + 1 in [6, 7]: # 6, 7이면 주말이라 이벤트 제외
                pass
            else:
                if cur_schedule + 10 < cur_timelog: # 출근시간에 한번이라도 늦었으면 이벤트 참여 불가
                    check = False 
            cur_day += 1
                
        if check == True:
            answer += 1 # 모든 날짜에 출근을 제대로 했으면 이벤트 참여 가능
            
    return answer

def test_solution():
    """테스트 케이스를 실행합니다."""
    # 테스트 케이스 1
    assert solution(
        [700, 800, 1100],
        [[710, 2359, 1050, 700, 650, 631, 659], 
         [800, 801, 805, 800, 759, 810, 809], 
         [1105, 1001, 1002, 600, 1059, 1001, 1100]],
        5
    ) == 3, "테스트 케이스 1 실패"
    
    # 테스트 케이스 2
    assert solution(
        [730, 855, 700, 720],
        [[710, 700, 650, 735, 700, 931, 912],
         [908, 901, 805, 815, 800, 831, 835],
         [705, 701, 702, 705, 710, 710, 711],
         [707, 731, 859, 913, 934, 931, 905]],
        1
    ) == 2, "테스트 케이스 2 실패"
    
    # 경계값 테스트
    assert solution([700], [[700, 700, 700, 700, 700, 700, 700]], 1) == 1, "경계값 테스트 1 실패"
    assert solution([1100], [[1100, 1100, 1100, 1100, 1100, 1100, 1100]], 7) == 1, "경계값 테스트 2 실패"
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 