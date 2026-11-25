class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        lowercase_s = s.lower()

        while r >= l:
            if not lowercase_s[l].isalnum():
                l += 1
                continue
            
            if not lowercase_s[r].isalnum():
                r -= 1
                continue

            if lowercase_s[l] == lowercase_s[r]:
                l += 1
                r -= 1
                continue

            return False

        return True
        