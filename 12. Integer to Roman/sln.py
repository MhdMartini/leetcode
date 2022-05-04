from typing import List
from timeit import timeit


class Solution:
    def intToRoman(self, num: int) -> str:
        denoms = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C',
                  'XC', 'L', 'CL', 'X', 'IX', 'V', 'IV', 'I']
        res = ""
        den_i = 0
        while num:
            for i, d in enumerate(denoms[den_i:]):
                num_romans = num // d
                if not num_romans:
                    continue

                res += romans[i + den_i] * num_romans
                break

            den_i = i + 1
            num %= d

        return res

    def intToRoman_v2(self, num: int) -> str:
        denoms = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C',
                  'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ""
        for i, d in enumerate(denoms):
            num_romans = num // d
            if not num_romans:
                continue
            res += romans[i] * num_romans
            num %= d

        return res


def main():
    # confirm
    num = 1994
    # sln1 = Solution().intToRoman(num)
    # sln2 = Solution().intToRoman_v2(num)
    # print(sln1, sln2)

    # time
    t1 = timeit(lambda: Solution().intToRoman(num))
    t2 = timeit(lambda: Solution().intToRoman_v2(num))
    print("v1:", t1)
    print("v2:", t2)


if __name__ == "__main__":
    main()
