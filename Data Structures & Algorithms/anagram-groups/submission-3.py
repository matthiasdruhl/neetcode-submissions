class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)

        for s in strs:
            bucket = [0] * 26
            for c in s:
                bucket[ord(c) - ord('a')] += 1
            check[tuple(bucket)].append(s)
        
        return list(check.values())
