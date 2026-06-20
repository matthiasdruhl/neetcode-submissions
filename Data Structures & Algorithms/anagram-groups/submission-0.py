class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        check = {}
        holder = 0
        for word in strs:
            temp = []
            for let in word:
                temp.append(let)
            temp.sort()
            t = ''
            for let in temp:
                t += let
            if t in check.keys():
                ans[check[t]].append(word)
            else:
                ans.append([word])
                check[t] = holder
                holder += 1
        return ans
