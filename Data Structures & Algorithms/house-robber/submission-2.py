class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        did,didnt = [0]*len(nums),[0]*len(nums)
        did[0]=nums[0]
        didnt[0]=0
        for i in range(1,len(nums)):
            did[i]=nums[i]+didnt[i-1]
            didnt[i]=max(did[i-1],didnt[i-1])
        return max(did[i],didnt[i])