class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while r > l:
            test = numbers[l] + numbers[r]
            if test == target:
                return [l + 1, r + 1]
            elif test > target:
                r -= 1
                continue
            else:
                l += 1

            
        return [-1, -1]

        # time = O(n), space = O(1)