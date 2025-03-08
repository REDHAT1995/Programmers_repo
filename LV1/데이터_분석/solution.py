from typing import List

def solution(data: List[List[int]], ext: str, val_ext: int, sort_by: str) -> List[List[int]]:
    """
    주어진 데이터에서 조건에 맞는 데이터를 추출하고 정렬하는 함수
    
    Args:
        data (List[List[int]]): [[코드 번호, 제조일, 최대 수량, 현재 수량], ...] 형태의 2차원 리스트
        ext (str): 데이터 추출 기준 ("code", "date", "maximum", "remain" 중 하나)
        val_ext (int): 추출 기준값
        sort_by (str): 정렬 기준 ("code", "date", "maximum", "remain" 중 하나)
    
    Returns:
        List[List[int]]: 조건에 맞게 필터링되고 정렬된 2차원 리스트
        
    Examples:
        >>> solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain")
        [[3, 20300401, 10, 8], [1, 20300104, 100, 80]]
    """
    answer = []

    # 데이터 컬럼 이름 표시
    data_name = ["code", "date", "maximum", "remain"]

    ext_index = data_name.index(ext) # 추출 기준 컬럼 인덱스
    filtered_data = [data[i] for i in range(len(data)) if data[i][ext_index] < val_ext]    # val_ext 보다 작은 데이터만 추출

    # 필터링 된 데이터를 sort_by 기준으로 오름차순 정렬
    sorted_data = sorted(filtered_data, key=lambda x: x[data_name.index(sort_by)])
    
    answer = sorted_data
    return answer

def test_solution():
    """
    solution 함수를 테스트하는 함수
    
    테스트 케이스:
    1. 기본 테스트 케이스
    2. 코드 번호 기준 필터링 및 정렬
    3. 최대 수량 기준 필터링 및 정렬
    4. 현재 수량 기준 필터링 및 정렬
    """
    # 테스트 케이스 1: 기본 케이스 (문제 예시)
    assert solution(
        [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
        "date",
        20300501,
        "remain"
    ) == [[3, 20300401, 10, 8], [1, 20300104, 100, 80]]
    
    # 테스트 케이스 2: 코드 번호 기준 필터링 및 정렬
    assert solution(
        [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
        "code",
        3,
        "date"
    ) == [[1, 20300104, 100, 80], [2, 20300804, 847, 37]]
    
    # 테스트 케이스 3: 최대 수량 기준 필터링 및 정렬
    assert solution(
        [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
        "maximum",
        500,
        "code"
    ) == [[1, 20300104, 100, 80], [3, 20300401, 10, 8]]
    
    # 테스트 케이스 4: 현재 수량 기준 필터링 및 정렬
    assert solution(
        [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
        "remain",
        50,
        "maximum"
    ) == [[3, 20300401, 10, 8], [2, 20300804, 847, 37]]
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 