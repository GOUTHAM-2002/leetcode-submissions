class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = list(zip(position,speed))
        fleet = sorted(fleet,reverse=True,key = lambda x : x[0])

        stack = []

        res = 0

        for pos,spd in fleet:
            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)
                res+=1
        return res
        