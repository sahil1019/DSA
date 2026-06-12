class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        missing = 3
        if any(c.islower() for c in password):
            missing -= 1
        if any(c.isupper() for c in password):
            missing -= 1
        if any(c.isdigit() for c in password):
            missing -= 1

        replace = 0
        one = two = 0

        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1

            length = j - i
            if length >= 3:
                replace += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1

            i = j

        if n < 6:
            return max(missing, 6 - n)

        if n <= 20:
            return max(missing, replace)

        delete = n - 20

        replace -= min(delete, one)
        delete -= min(delete, one)

        use = min(delete, two * 2)
        replace -= use // 2
        delete -= use

        replace -= delete // 3

        return (n - 20) + max(missing, replace)