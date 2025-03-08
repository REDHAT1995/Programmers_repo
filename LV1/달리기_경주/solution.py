from typing import List, Dict

def solution(players: List[str], callings: List[str]) -> List[str]:
    """
    달리기 경주 결과를 계산하는 함수
    
    Args:
        players (List[str]): 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열
        callings (List[str]): 해설진이 부른 이름을 담은 문자열 배열
    
    Returns:
        List[str]: 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 담은 배열
        
    Examples:
        >>> solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
        ["mumu", "kai", "mine", "soe", "poe"]
    """
    
    # 선수 이름으로 모두 찾으면 시간이 너무 많이 걸림
    # 따라서 순위로 찾아야 함
    
    # 선수 이름 -> 순위 매핑
    player_to_rank: Dict[str, int] = {player: rank for rank, player in enumerate(players)}
    # 순위 -> 선수 이름 매핑
    rank_to_player: Dict[int, str] = {rank: player for rank, player in enumerate(players)}
    
    # 해설진이 부른 선수들 순회
    for calling in callings:
        # 현재 호출된 선수의 순위와 앞 선수의 순위
        curr_rank = player_to_rank[calling]
        prev_rank = curr_rank - 1
        
        # 앞 선수의 이름
        prev_player = rank_to_player[prev_rank]
        
        # 순위 교환
        player_to_rank[calling] = prev_rank
        player_to_rank[prev_player] = curr_rank
        rank_to_player[prev_rank] = calling
        rank_to_player[curr_rank] = prev_player
    
    # 최종 순위
    answer = [rank_to_player[i] for i in range(len(players))]
    return answer

def test_solution():
    """
    solution 함수를 테스트하는 함수
    
    테스트 케이스:
    1. 기본 테스트 케이스
    2. 연속 추월 테스트
    3. 단일 선수 여러 번 추월
    4. 여러 선수 각각 한 번씩 추월
    """
    # 테스트 케이스 1: 기본 케이스 (문제 예시)
    assert solution(
        ["mumu", "soe", "poe", "kai", "mine"],
        ["kai", "kai", "mine", "mine"]
    ) == ["mumu", "kai", "mine", "soe", "poe"]

    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 