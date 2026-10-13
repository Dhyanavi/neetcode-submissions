import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = collections.defaultdict(list)
        for s in strs:
            s_sorted = "".join(sorted(s))
            anagram_map[s_sorted].append(s)
        return list(anagram_map.values())
