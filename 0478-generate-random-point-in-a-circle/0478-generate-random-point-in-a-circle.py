import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        theta = random.random() * 2 * math.pi
        dist = math.sqrt(random.random()) * self.r

        return [
            self.x + dist * math.cos(theta),
            self.y + dist * math.sin(theta)
        ]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()