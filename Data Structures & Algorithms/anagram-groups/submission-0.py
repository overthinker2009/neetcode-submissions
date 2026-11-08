class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if Counter(i) == Counter(j):
                    return [i, j]