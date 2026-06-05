class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<3:
            return min(nums)
        l,r=0,len(nums) - 1
        res=float('inf')
        temp=0
        while l < r:
            mid = l + (r-l) // 2
            a,b,c = nums[l],nums[mid],nums[r]
            temp=min(nums[l],nums[mid],nums[r])
            res=min(res,temp)
            if a == temp:
                r=mid-1
            elif c == temp:
                l=mid+1
            else:
                if nums[l] == max(nums[l],nums[mid],nums[r]):
                    r=mid-1
                else:
                    l=mid+1
        return res



        