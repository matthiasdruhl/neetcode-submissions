class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = ""
        leng = min(len(strs[0]), len(strs[-1]))
        curr = 0
        while curr < leng:
            if strs[0][curr] == strs[-1][curr]:
                ans += strs[0][curr]
                curr += 1
            else:
                break
        return ans