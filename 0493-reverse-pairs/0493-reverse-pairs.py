class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, cnt1 = merge_sort(arr[:mid])
            right, cnt2 = merge_sort(arr[mid:])

            cnt = cnt1 + cnt2

            j = 0
            for x in left:
                while j < len(right) and x > 2 * right[j]:
                    j += 1
                cnt += j

            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, cnt

        return merge_sort(nums)[1]