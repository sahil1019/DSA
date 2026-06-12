class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        res = 0

        for house in houses:
            left, right = 0, len(heaters)

            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid

            d1 = float('inf') if left == len(heaters) else abs(heaters[left] - house)
            d2 = float('inf') if left == 0 else abs(house - heaters[left - 1])

            res = max(res, min(d1, d2))

        return res