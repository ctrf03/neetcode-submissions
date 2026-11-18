class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def makeKey(s: str) -> List[int]:
            key = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                key[i] += 1
            return key

        hashmap = defaultdict(list)
        
        for s in strs:
            key = tuple(makeKey(s))
            hashmap[key].append(s)
        
        return list(hashmap.values())