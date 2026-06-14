class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)

        if total % n:
            return -1

        avg = total // n
        ans = 0
        balance = 0

        for dresses in machines:
            balance += dresses - avg
            ans = max(ans, abs(balance), dresses - avg)

        return ans