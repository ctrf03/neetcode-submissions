class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        n = len(nums)

        for i in range(n):
            key = target - nums[i]
            if key in map:
                return [map[key], i]
            else:
                map[nums[i]] = i
