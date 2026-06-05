class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(n^2) time complexity
        res = []
        for i in range(len(nums)):
            output=1
            for j in range(len(nums)):
                if i!=j:
                    output*=nums[j]
            res.append(output)
        return res


        