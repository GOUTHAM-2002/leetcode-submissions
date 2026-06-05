class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        temp = min(strs, key=len)

        for word in strs:
            a = 0

            while a < len(temp) and a < len(word) and word[a] == temp[a]:
                a += 1

            temp = temp[:a]

            if temp == "":
                return ""

        return temp