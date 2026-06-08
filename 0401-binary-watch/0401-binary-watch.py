from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []

        def backtrack(pos, leds, hours, minutes):
            if hours > 11 or minutes > 59:
                return

            if leds == 0:
                res.append(f"{hours}:{minutes:02d}")
                return

            for i in range(pos, 10):
                if i < 4:  # hour LEDs
                    backtrack(i + 1, leds - 1, hours + (1 << i), minutes)
                else:      # minute LEDs
                    backtrack(i + 1, leds - 1, hours, minutes + (1 << (i - 4)))

        backtrack(0, turnedOn, 0, 0)
        return res