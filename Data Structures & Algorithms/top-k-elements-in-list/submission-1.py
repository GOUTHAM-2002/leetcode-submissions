class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            dic[i] = dic.get(i,0) + 1
        for n,v in dic.items():
            freq[v].append(n)
        res = []
        for i in range(len(freq) -1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        