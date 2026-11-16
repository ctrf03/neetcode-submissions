class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = dict()

        for i in nums:
            if i in map:
                return True
            else:
                map[i] = 1
        
        return False
        