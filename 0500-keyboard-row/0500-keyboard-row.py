class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        res = []

        for word in words:
            w = set(word.lower())
            if any(w <= row for row in rows):
                res.append(word)

        return res