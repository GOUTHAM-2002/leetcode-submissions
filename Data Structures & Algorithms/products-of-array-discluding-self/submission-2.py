class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n^2) time complexity
        # res = []
        # for i in range(len(nums)):
        #     output=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             output*=nums[j]
        #     res.append(output)
        # return res




        # O(n) with using division operator
        # zero_cnt = 0
        # zero_pos = 0
        # temp = 1
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zero_cnt+=1
        #         zero_pos = i
        #     else:
        #         temp*=nums[i]
        # if zero_cnt > 1:
        #     return [0] * len(nums)
        # elif zero_cnt == 1:
        #     output = [0] *len(nums)
        #     output[zero_pos] = temp
        #     return output
        # else:
        #     output = [temp] * len(nums)
        #     for i in range(len(nums)):
        #         output[i]//=nums[i]
        #     return output



        #O(n) without using the division operator

        prefix,suffix = [1]*len(nums),[1]*len(nums)
        temp = nums[0]
        for i in range(1,len(nums)):
            prefix[i]*=temp
            temp*=nums[i]
        temp = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i]*=temp
            temp*=nums[i]
        return [a*b for a,b in zip(prefix,suffix)]






        