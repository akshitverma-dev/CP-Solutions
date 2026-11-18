class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        freq = {}
        for i in strs:
            if i not in freq:
                freq[i] = {}
                for k in i:
                    if k not in freq[i]:
                        freq[i][k] = 1
                    else:
                        freq[i][k] += 1
        fset = {frozenset(d.items()) for d in freq.values()}
        # print(fset)
        for i in fset:
            target = dict(i)
            matching_keys = [word for word in strs if freq[word] == target]
            result.append(matching_keys)

        return (result)




