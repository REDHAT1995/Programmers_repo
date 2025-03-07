def solution(friends: list, gifts: list) -> int:
    """
    다음 달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 계산하는 함수
    
    Args:
        friends (list): 친구들의 이름을 담은 문자열 배열
        gifts (list): 이번 달까지 친구들이 주고받은 선물 기록을 담은 문자열 배열
        
    Returns:
        int: 다음 달에 가장 많은 선물을 받는 친구가 받을 선물의 수
        
    Examples:
        >>> solution(["muzi", "ryan", "frodo", "neo"], 
                    ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", 
                     "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
        2
    """
    answer = 0
    # 각 친구들이 선물을 주는 횟수를 저장하는 딕셔너리, 초기화
    gift_count = {}
    for cur_friend in friends:
        gift_count[cur_friend] = {friend: 0 for friend in friends if friend != cur_friend}    # 각 친구 딕셔너리에 자기를 제외한 친구들을 키로 추가하고 값을 0으로 초기화
        gift_count[cur_friend]["gived"] = 0  # 주는 선물 횟수
        gift_count[cur_friend]["received"] = 0  # 받는 선물 횟수
        gift_count[cur_friend]["will_receive"] = 0  # 다음 달에 받을 선물 횟수
        
    # 주고받은 선물 기록을 확인하여 각 친구들의 선물 횟수를 증가
    for gift in gifts:
        giver, receiver = gift.split()
        gift_count[giver][receiver] += 1
        gift_count[giver]["gived"] += 1
        gift_count[receiver]["received"] += 1
        
    # 선물 지수 계산
    for friend in friends:
        gift_count[friend]["gift_point"] = gift_count[friend]["gived"] - gift_count[friend]["received"]
        
    # 다음달에  받을 선물 계산
    for cur_friend in friends:
        for friend in [f for f in friends if f != cur_friend]: # 모든 친구들 순회
            if gift_count[cur_friend][friend] > gift_count[friend][cur_friend]: # 다른 친구에게 선물을 많이 줬다면
                gift_count[cur_friend]["will_receive"] += 1
            elif gift_count[cur_friend][friend] == gift_count[friend][cur_friend]: # 선물을 주고받은 횟수가 같다면
                # 선물 지수가 높은 친구가 선물을 받는다.
                if gift_count[cur_friend]["gift_point"] > gift_count[friend]["gift_point"]:
                    gift_count[cur_friend]["will_receive"] += 1
                
    # 가장 많이 선물을 받는 친구의 선물 개수 계산 및 반환
    answer = max(gift_count[friend]["will_receive"] for friend in friends)
    return answer
                    
# 테스트 케이스
def test_solution():
    """
    solution 함수를 테스트하는 함수
    """
    # 테스트 케이스 1
    assert solution(
        ["muzi", "ryan", "frodo", "neo"],
        ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", 
         "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    ) == 2
    
    # 테스트 케이스 2
    assert solution(
        ["joy", "brad", "alessandro", "conan", "david"],
        ["alessandro brad", "alessandro joy", "alessandro conan", 
         "david alessandro", "alessandro david"]
    ) == 4
    
    # 테스트 케이스 3
    assert solution(
        ["a", "b", "c"],
        ["a b", "b a", "c a", "a c", "a c", "c a"]
    ) == 0
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 