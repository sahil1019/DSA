from collections import defaultdict
import random

class Solution:

    def __init__(self, nums):
        self.indices = defaultdict(list)

        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target):
        return random.choice(self.indices[target])