class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False

            for p in parts:
                if not p or (len(p) > 1 and p[0] == '0'):
                    return False
                if not p.isdigit():
                    return False
                if not 0 <= int(p) <= 255:
                    return False

            return True

        def isIPv6(ip):
            hex_digits = "0123456789abcdefABCDEF"
            parts = ip.split(':')
            if len(parts) != 8:
                return False

            for p in parts:
                if not (1 <= len(p) <= 4):
                    return False
                if any(c not in hex_digits for c in p):
                    return False

            return True

        if isIPv4(queryIP):
            return "IPv4"
        if isIPv6(queryIP):
            return "IPv6"
        return "Neither"