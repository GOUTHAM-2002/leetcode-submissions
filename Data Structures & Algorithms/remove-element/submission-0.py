class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j=0,0
        while i < len(nums) and nums[i]!=val:
            i+=1
        if i >=len(nums):
            return len(nums)
        if i == (len(nums)-1):
            nums=nums[:-1]
            return len(nums)
        j=i+1
        while j < len(nums) and nums[j]==val:
            j+=1

        if j >=len(nums):
            nums=nums[:i]
            return len(nums)
        while j < len(nums):
            nums[i]=nums[j]
            i+=1
            j+=1
            while j < len(nums) and nums[j]==val:
                j+=1
        nums=nums[:i]
        return len(nums)
        