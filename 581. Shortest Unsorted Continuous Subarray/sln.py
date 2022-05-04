from re import S
from typing import List
from timeit import timeit
from itertools import combinations


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i, j = self.find_bounds(nums, len(nums))
        if i == j:
            return 0
        return j - i + 1

    def find_bounds(self, nums, len_nums):
        l = self.find_l(nums, len_nums)
        r = self.find_r(l, nums, len_nums)
        return l, r

    def find_l(self, nums, len_nums):
        l = 0
        for i in range(len_nums - 1):
            if nums[l] > nums[i + 1]:
                return l
            elif nums[l] < nums[i + 1]:
                l = i + 1
        return 0

    def find_r(self, l, nums, len_nums):
        r = l + 1
        start = False
        for i in range(r, len_nums - 1):
            if nums[i] >= nums[i + 1]:
                if start:
                    r = i + 1
                elif nums[i] > nums[i + 1]:
                    start = True

        return r

    def findUnsortedSubarray_v2(self, nums: List[int]) -> int:
        # Sort the given array
        return self.findUnsortedSubarray(nums)


def main():
    # confirm
    nums = [1, 2, 3, 3, 3]
    sln1 = Solution().findUnsortedSubarray(nums)
    sln2 = Solution().findUnsortedSubarray_v2(nums)
    print(sln1)
    print(sln2)

    # time
    # t1 = timeit(lambda: Solution().threeSum(nums))
    # t2 = timeit(lambda: Solution().threeSum(nums))
    # print("v1:", t1)
    # print("v2:", t2)


if __name__ == "__main__":
    main()
