class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)

        res = 0

        for n in unique:
            if n - 1 not in unique:
                next = n + 1
                count = 1
                while next in unique:
                    count += 1
                    next += 1
                res = max(res, count)

        return res

        # time = O(n), space = O(n)