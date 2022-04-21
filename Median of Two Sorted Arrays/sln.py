from typing import List
from timeit import timeit


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        nums = []
        while True:
            if i >= m and j >= n:
                return self.get_median(nums)
            if i >= m:
                nums.append(nums2[j])
                j += 1
            elif j >= n:
                nums.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

    def findMedianSortedArrays_v2(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        return self.get_median(nums)

    def get_median(self, nums: List[int]) -> float:
        m = len(nums)
        mid = m // 2
        if m % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            return nums[mid]


def main():
    nums1 = [1, 3]
    nums2 = [2, 4]
    t1 = timeit(lambda: Solution().findMedianSortedArrays(nums1, nums2))
    t2 = timeit(lambda: Solution().findMedianSortedArrays_v2(nums1, nums2))

    median = Solution().findMedianSortedArrays(nums1, nums2)
    print(median)
    print("v1:", t1)
    print("v2:", t2)


if __name__ == "__main__":
    main()
