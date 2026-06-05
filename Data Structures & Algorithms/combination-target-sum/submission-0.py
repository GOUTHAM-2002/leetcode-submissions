
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, summ, temp):
            if summ == target:
                res.append(temp.copy())  # Append a copy of temp
                return
            elif summ > target:
                return
            
            for i in range(start, len(nums)):  # Allow choosing the same element again
                # Include the number and move forward
                temp.append(nums[i])
                backtrack(i, summ + nums[i], temp)  # Allow the same index
                temp.pop()  # Backtrack
        
        backtrack(0, 0, [])
        return res