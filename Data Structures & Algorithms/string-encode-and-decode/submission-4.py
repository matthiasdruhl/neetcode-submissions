class Solution:

    def encode(self, strs: List[str]) -> str:
        comb = ""
        for word in strs:
            comb += "Fuck" + word
        return comb

    def decode(self, s: str) -> List[str]:
        return (s.split("Fuck"))[1:]
