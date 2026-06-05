class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        meow = set()
        for i in nums:
            if i in meow:
                return True
            else:
                meow.add(i)
        return False


         