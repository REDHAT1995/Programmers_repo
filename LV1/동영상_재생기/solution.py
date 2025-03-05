from typing import List

def time_to_seconds(time_str: str) -> int:
    """
    "mm:ss" 형식의 시간 문자열을 초 단위로 변환하는 함수
    
    Args:
        time_str (str): "mm:ss" 형식의 시간 문자열
        
    Returns:
        int: 초 단위로 변환된 시간
    """
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def seconds_to_time(seconds: int) -> str:
    """
    초 단위의 시간을 "mm:ss" 형식의 문자열로 변환하는 함수
    
    Args:
        seconds (int): 초 단위의 시간
        
    Returns:
        str: "mm:ss" 형식의 시간 문자열
    """
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

def solution(video_len: str, pos: str, op_start: str, op_end: str, commands: List[str]) -> str:
    """
    동영상 재생기의 명령어를 처리하는 함수
    
    Args:
        video_len (str): 동영상의 전체 길이 (mm:ss 형식)
        pos (str): 현재 재생 위치 (mm:ss 형식)
        op_start (str): 오프닝 시작 시각 (mm:ss 형식)
        op_end (str): 오프닝 종료 시각 (mm:ss 형식)
        commands (List[str]): 실행할 명령어 리스트 ("prev" 또는 "next")
        
    Returns:
        str: 최종 재생 위치 (mm:ss 형식)
    """
    # 1. 모든 시간 문자열을 초 단위로 변환
    current_pos = time_to_seconds(pos)
    video_length = time_to_seconds(video_len)
    op_start_seconds = time_to_seconds(op_start)
    op_end_seconds = time_to_seconds(op_end)
    
    # 2. 명령어 처리
    for command in commands:
        # 2.1 오프닝 구간 체크
        if op_start_seconds <= current_pos <= op_end_seconds:
            current_pos = op_end_seconds
            
        # 2.2 명령어 처리
        if command == "prev":
            current_pos = max(0, current_pos - 10)
        elif command == "next":
            current_pos = min(video_length, current_pos + 10)
    
    # 3. 최종 오프닝 구간 체크
    if op_start_seconds <= current_pos <= op_end_seconds:
        current_pos = op_end_seconds
    
    # 4. 최종 위치를 "mm:ss" 형식으로 변환하여 반환
    return seconds_to_time(current_pos)

def test_solution():
    """
    solution 함수의 테스트를 수행하는 함수
    """
    # 테스트 케이스 1
    assert solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]) == "13:00"
    assert solution("07:22", "04:05", "00:15", "04:07", ["next"]) == "04:17"
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 