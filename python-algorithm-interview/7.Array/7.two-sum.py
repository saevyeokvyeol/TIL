from typing import List

class Solution:
    # 내 풀이(브루트 포스...?)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                idx = nums.index(target - nums[i])
                if idx >= i and i != idx:
                    return [i, idx]
            except:
                pass

    # 브루트 포스
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    # 시간이 좀 더 걸리기는 하지만 코드가 훨씬 간결하다

    # in을 이용한 탐색
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
    # 인덱스와 해당 인덱스 원소를 튜플로 묶어 리스트로 반환하는 enumerate() 함수를 이용한 풀이

    # 첫 번째 수를 뺀 결과 키 조회
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]