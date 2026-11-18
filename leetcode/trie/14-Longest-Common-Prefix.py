class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        ps = True
        num = 0
        while ps:
            try:
                cur = strs[0][num]
                for i in strs:
                    if i[num] != cur:
                        ps=False  
                        break
                if ps == True:
                
                    result +=cur
                num+=1
            except IndexError:
                ps= False
        return result
                