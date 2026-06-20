class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        print("encoded_string: " + encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        l = 0
        r = 0
        while l < len(s):
            while s[r] != "#":
                r += 1
            print(s[l:r])
            length = int(s[l:r])
            l = r + 1
            r = l + length
            decoded.append(s[l:r])
            l = r
        return decoded
           

        