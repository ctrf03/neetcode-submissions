class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = dict()

        for c in s:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1

        for c in t:
            if c not in map or map[c] == 0:
                return False
            else:
                map[c] -= 1

        return True