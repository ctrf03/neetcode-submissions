class Solution:

    def encode(self, strs: List[str]) -> str:
        ct = ""

        for s in strs:
            l = len(s)
            ct += str(l) + '#' + s

        return ct

    def decode(self, s: str) -> List[str]: 
        pt = []
        counter = 0
        string = ""

        for i in range(len(s)):
            if counter == 0:
                if s[i] != '#': 
                    string += s[i]
                    continue
                else:
                    counter = int(string)
                    string = ""

                    if counter == 0:
                        pt.append("")
                    continue
                
            string += s[i]
            counter -= 1

            if counter == 0:
                pt.append(string)
                string = ""

        return pt
