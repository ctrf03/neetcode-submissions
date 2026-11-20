class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        zero_id = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                zero_id = i
                continue
            prod *= nums[i]

        if zero_count > 1:
            return [0] * len(nums)
        
        if zero_count == 1:
            res = [0] * len(nums)
            res[zero_id] = prod
            return res

        res = []

        for n in nums:
            res.append(int(prod / n))

        return res
        