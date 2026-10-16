class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s))
            result += "|"
            result += s

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            temp = i
            while s[temp] != "|":
                temp += 1
            
            length = int(s[i:temp])
            start = temp + 1
            end = start + length

            result.append(s[start:end])
            i = end
        
        return result

