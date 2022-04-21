from typing import List
from timeit import timeit


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        smallest = 0
        for num in nums:
            if num < 1:
                continue
            if num - smallest > 1:
                break
            smallest = num
        return smallest + 1

    def firstMissingPositive_v2(self, nums: List[int]) -> int:
        nums_s = sorted(nums)
        smallest = 0
        for num in nums_s:
            if num - smallest > 1:
                break
            smallest = num
        return smallest + 1


def main():
    nums = [0, 2, 2, 1, 1]
    t1 = timeit(lambda: Solution().firstMissingPositive(nums))
    t2 = timeit(lambda: Solution().firstMissingPositive_v2(nums))
    print("v1:", t1)
    print("v2:", t2)

    sln = Solution().firstMissingPositive_v2(nums)
    print(sln)


if __name__ == "__main__":
    main()
