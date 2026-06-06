class Solution:
    def countBits(self, n: int) -> List[int]:
        temp = []
        for i in range(n+1):
            temp.append(bin(i).count('1'))
        return temp
        