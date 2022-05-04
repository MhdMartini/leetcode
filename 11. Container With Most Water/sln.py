from typing import List
from timeit import timeit


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            area = max(area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area


def main():
    # confirm
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sln = Solution().maxArea(height)
    print(sln)

    # time
    t1 = timeit(lambda: Solution().maxArea(height))
    # t2 = timeit(lambda: Solution().maxArea(height))
    print("v1:", t1)
    # print("v2:", t2)


if __name__ == "__main__":
    main()
