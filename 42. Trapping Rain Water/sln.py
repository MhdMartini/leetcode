from typing import List
from timeit import timeit


class Solution:
    def trap(self, height: List[int]) -> int:
        sum_total = 0
        stack = []
        height_len = len(height)
        for i in range(height_len):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                distance = i - stack[-1] - 1
                sum_total += (min(height[i], height[stack[-1]]
                                  ) - height[top]) * distance
            stack.append(i)
        return sum_total

    def trap_v2(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size
        left_max[0] = height[0]
        for i in range(1, size, 1):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, size - 1, 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [4, 2, 3]
    # t1 = timeit(lambda: Solution().trap(height))
    # t2 = timeit(lambda: Solution().trap(height))
    # print("v1:", t1)
    # print("v2:", t2)

    sln = Solution().trap(height)
    print(sln)


if __name__ == "__main__":
    main()
