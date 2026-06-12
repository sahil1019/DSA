class Solution:
    def makesquare(self, matchsticks):
        total = sum(matchsticks)

        if total % 4:
            return False

        target = total // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return all(side == target for side in sides)

            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]

                if sides[j] == 0:
                    break

            return False

        return dfs(0)