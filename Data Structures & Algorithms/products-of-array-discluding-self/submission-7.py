class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        res = []

        prev = 1

        for n in nums:
            pre.append(prev)
            prev *= n

        prev = 1

        for i in range(len(nums) - 1, -1, -1):
            suf.append(prev)
            prev *= nums[i]

        suf.reverse()

        for i in range(len(nums)):
            res.append(pre[i] * suf[i])

        return res 
            

             
        