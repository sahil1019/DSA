class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = [0]  # length at each depth
        ans = 0

        for item in input.split('\n'):
            depth = item.count('\t')
            name = item.lstrip('\t')

            while len(stack) > depth + 1:
                stack.pop()

            curr_len = stack[-1] + len(name)

            if '.' in name:  # file
                ans = max(ans, curr_len)
            else:  # directory
                stack.append(curr_len + 1)  # +1 for '/'

        return ans