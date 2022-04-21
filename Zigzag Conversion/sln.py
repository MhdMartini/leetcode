from typing import List
from timeit import timeit


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lines = [""] * numRows
        i, i_s = 0, 0
        up = True
        if numRows == 1:
            return s
        while True:
            if i_s >= len(s):
                return "".join(lines)
            lines[i] += s[i_s]
            if i == 0 or i == numRows - 1:
                up = not up
            i = i - up + (not up)
            i_s += 1

    def convert_v2(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
        lines = [""] * numRows

        i, count, len_s, down = 0, 0, len(s), False
        lines[0] = s[0]
        for count in range(len_s - 1):
            if not (count % (numRows - 1)):
                down = not down
            di = 1 if down else numRows - 1
            i += di
            lines[i % numRows] += s[count + 1]
        return "".join(lines)


def main():
    s = "PAYPALISHIRING"
    numRows = 3
    t1 = timeit(lambda: Solution().convert(s, numRows))
    t2 = timeit(lambda: Solution().convert_v2(s, numRows))

    sln = Solution().convert_v2(s, numRows)
    print(sln)
    print("v1:", t1)
    print("v2:", t2)


if __name__ == "__main__":
    main()
