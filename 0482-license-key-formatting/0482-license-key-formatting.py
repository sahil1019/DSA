class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        res = []

        for i, ch in enumerate(reversed(s)):
            if i and i % k == 0:
                res.append('-')
            res.append(ch)

        return ''.join(reversed(res))