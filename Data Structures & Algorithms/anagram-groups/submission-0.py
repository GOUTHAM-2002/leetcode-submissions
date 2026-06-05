class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)):
            temp="".join(sorted(strs[i]))
            if temp in dic:
                dic[temp].append(i)
            else:
                dic[temp] = [i]

        res=[]
        temp_res=[]
        for key,values in dic.items():
            for i in values:
                temp_res.append(strs[i])
            res.append(temp_res)
            temp_res=[]
        return res



        

        