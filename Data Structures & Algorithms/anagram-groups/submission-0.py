class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for w in strs:
            k = "".join(sorted(w))
            d[k] += [w]
        res = []
        for k,v in d.items():
            res.append(v)
        return res
        


