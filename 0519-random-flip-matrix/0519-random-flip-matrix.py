import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.reset()

    def flip(self) -> List[int]:
        r = random.randint(0, self.total - 1)

        x = self.mp.get(r, r)
        self.total -= 1
        self.mp[r] = self.mp.get(self.total, self.total)

        return [x // self.n, x % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.mp = {}