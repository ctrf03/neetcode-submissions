class Solution:

    def encode(self, strs: List[str]) -> str:
        ct = ""

        for s in strs:
            ct += str(len(s)) + '#' + s

        return ct

    def decode(self, s: str) -> List[str]:
        pt = []
        count = 0
        aux = ""

        for c in s:
            if count == 0:
                if c == '#':
                    count = int(aux)
                    aux = ""
                    if count == 0:
                        pt.append(aux)
                    continue
                aux += c
                continue
            
            aux += c
            count -= 1

            if count == 0:
                pt.append(aux)
                aux = ""

        return pt
            
            
