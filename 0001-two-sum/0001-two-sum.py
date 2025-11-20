class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # 숫자: 인덱스 저장
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i