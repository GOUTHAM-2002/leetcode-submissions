class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # solving it in O(nlog(n)) runtime
        if not nums:
            return 0
        nums = sorted(nums)
        print(nums)
        res=0
        temp=0
        init = nums[0]-1
        for i in nums:
            if i == init:
                continue
            elif i - 1 == init:
                temp+=1
                init = i
            else:
                res= max(res,temp)
                init = i
                temp=1
        return max(res,temp)

        