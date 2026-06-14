class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        m = len(flowerbed)

        for i in range(m):
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i - 1] == 0) and
                (i == m - 1 or flowerbed[i + 1] == 0)):
                
                flowerbed[i] = 1
                count += 1

        return count >= n