class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        freq = {}
        for i in strs:
            srtd = "".join(sorted(i))
            if srtd not in freq:
                freq[srtd] = []
                freq[srtd].append(i)
            else:
                freq[srtd].append(i)

        return(list(freq.values()))




