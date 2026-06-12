from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def nxt(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = fast = i
            direction = nums[i] > 0

            while True:
                ns = nxt(slow)
                nf = nxt(fast)

                if (nums[slow] > 0) != direction or (nums[ns] > 0) != direction:
                    break

                if (nums[fast] > 0) != direction or (nums[nf] > 0) != direction:
                    break

                nf2 = nxt(nf)
                if (nums[nf2] > 0) != direction:
                    break

                slow = ns
                fast = nf2

                if slow == fast:
                    if slow == nxt(slow):
                        break
                    return True

            j = i
            while (nums[j] > 0) == direction and nums[j] != 0:
                nxt_j = nxt(j)
                nums[j] = 0
                j = nxt_j

        return False