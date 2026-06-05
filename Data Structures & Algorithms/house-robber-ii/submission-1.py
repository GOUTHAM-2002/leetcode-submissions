class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        did1,didnt1,did2,didnt2=0,0,0,0
        for i in nums[1:]:
            temp=did1
            did1=i+didnt1
            didnt1=max(temp,didnt1)
        for i in nums[:-1]:
            temp=did2
            did2=i+didnt2
            didnt2=max(temp,didnt2)
        return max(did1,didnt1,did2,didnt2)

        