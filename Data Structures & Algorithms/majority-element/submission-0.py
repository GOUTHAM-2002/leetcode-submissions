class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter,pointer=0,"x"
        for num in nums:
            if pointer=="x":
                counter=1
                pointer=num
            else:
                if pointer == num:
                    counter +=1
                else:
                    if counter < 1:
                        pointer = num
                        counter=1
                    else:
                        counter-=1
        return pointer



        