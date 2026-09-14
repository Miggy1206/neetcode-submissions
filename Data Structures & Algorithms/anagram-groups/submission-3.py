class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        l = []
        for str in strs:
            sorted_str_copy = "".join(sorted(str[:]))
            if sorted_str_copy in m:
                m[sorted_str_copy].append(str)
            else:
                m[sorted_str_copy]=[str]


        return list(m.values())