from typing import List

class Sorting:

    def mergesort(self, nums: List[int]) -> List[int]:
        # base case, zero or one element
        if len(nums) <= 1:
            return nums

        pivot = len(nums) // 2
        left_arr = self.mergesort(nums[:pivot])
        right_arr = self.mergesort(nums[pivot:])

        return self.merge(left_arr, right_arr)

    def merge(self, left_arr, right_arr):
        i, j = 0, 0
        res = []
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                res.append(left_arr[i])
                i += 1
            else:
                res.append(right_arr[j])
                j += 1

        res.extend(left_arr[i:])
        res.extend(right_arr[j:])
        return res

    def partition(self, arr, l, r):
        pivot = arr[r]
        i = l - 1
        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i + 1

    def quicksort(self, nums: List[int], l: int, r: int) -> List[int]:
        if l >= r:
            return

        pivot = self.partition(nums, l, r)

        self.quicksort(nums, l, pivot - 1)
        self.quicksort(nums, pivot + 1, r)


if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    obj = Sorting()
    print(obj.mergesort(nums))