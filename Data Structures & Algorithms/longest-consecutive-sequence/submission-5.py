class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = dict.fromkeys(nums, 0)
        longest = 0

        for n in hashmap:
            if n - 1 not in hashmap:
                aux = 1
                next = n + 1
                while next in hashmap:
                    aux += 1
                    next += 1
                longest = max(longest, aux)
        
        return longest
                