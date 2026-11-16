class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def makeKey(s: str) -> List[int]:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            return counts

        hashmap = defaultdict(list)

        for s in strs:
            key = tuple(makeKey(s))
            hashmap[key].append(s)
    
        return list(hashmap.values())
            


