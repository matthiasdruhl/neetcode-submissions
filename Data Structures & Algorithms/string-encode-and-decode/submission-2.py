class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for strss in strs:
            ans += "FUCK"
            ans += strss
        return ans

    def decode(self, s: str) -> List[str]:
        s = s.split("FUCK")
        return s[1:]