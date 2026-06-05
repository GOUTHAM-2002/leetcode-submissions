class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        temp = []
        for key,values in dic.items():
            temp.append([key,values])
        temp = sorted(temp,key= lambda x : x[1],reverse=True)
        res=[]
        for i in range(k):
            meow = temp.pop(0)
            res.append(meow[0])
        return res
        