class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        if not nums or len(nums) < 2:   return []
        for i,n in enumerate(nums):
            if n in d:  return [d[n], i]
            d[target-n] = i
        return []
        