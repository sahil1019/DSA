from collections import Counter
from functools import lru_cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = Counter(hand)

        def remove(s):
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    return remove(s[:i] + s[j:])
                i = j
            return s

        @lru_cache(None)
        def dfs(board, state):
            if not board:
                return 0

            cnt = Counter()
            for i in range(0, len(state), 2):
                cnt[state[i]] = int(state[i + 1])

            ans = float('inf')

            for i in range(len(board) + 1):
                for c in cnt:
                    if cnt[c] == 0:
                        continue

                    if i > 0 and board[i - 1] == c:
                        continue

                    if (i < len(board) and board[i] == c) or (
                        0 < i < len(board) and board[i - 1] == board[i] != c
                    ):
                        cnt[c] -= 1

                        new_state = ''.join(
                            k + str(cnt[k]) for k in sorted(cnt)
                        )

                        nxt = remove(board[:i] + c + board[i:])
                        t = dfs(nxt, new_state)

                        if t != -1:
                            ans = min(ans, t + 1)

                        cnt[c] += 1

            return -1 if ans == float('inf') else ans

        state = ''.join(c + str(hand[c]) for c in sorted(hand))
        return dfs(board, state)