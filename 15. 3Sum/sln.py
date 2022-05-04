from typing import List
from timeit import timeit
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        result = {}
        for i, n in enumerate(nums[:-2]):
            l = i + 1
            r = len_nums - 1
            while l < r:
                tup = (n, nums[l], nums[r])
                if result.get(tup):
                    l, r = l + 1, r - 1
                    continue

                nums_sum = sum(tup)
                if nums_sum == 0:
                    result[tup] = True
                    l, r = l + 1, r - 1
                elif nums_sum < 0:
                    l += 1
                else:
                    r -= 1
        return list(result.keys())

    def threeSum_v2(self, nums: List[int]) -> List[List[int]]:
        # Sort the given array
        nums.sort()
        result = {}
        for combo in combinations(nums, 3):
            if result.get(combo) or sum(combo) != 0:
                continue
            result[combo] = True
        return list(result.keys())


def main():
    # confirm
    nums = [-1, 0, 1, 2, -1, -4]
    sln1 = Solution().threeSum(nums)
    sln2 = Solution().threeSum_v2(nums)
    print(sln1)
    print(sln2)

    # time
    t1 = timeit(lambda: Solution().threeSum(nums))
    t2 = timeit(lambda: Solution().threeSum(nums))
    print("v1:", t1)
    print("v2:", t2)


if __name__ == "__main__":
    main()
