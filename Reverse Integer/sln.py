from timeit import timeit


class Solution:
    def reverse(self, x: int) -> int:
        lb = -2 ** 31
        ub = -lb - 1
        xs = str(x)
        if xs[0] == '-':
            xs = xs[1:]
            xs = xs[::-1]
            xs = '-' + xs
        else:
            xs = xs[::-1]

        y = int(xs)
        if not lb < y < ub:
            return 0
        return y

    def reverse_v2(self, x: int) -> int:
        lb = -2 ** 31
        ub = -lb - 1
        xs = str(x)
        if x < 0:
            xs = xs[1:]
            xs = xs[::-1]
            xs = '-' + xs
        else:
            xs = xs[::-1]

        y = int(xs)
        if not lb < y < ub:
            return 0
        return y


def main():
    x = -120
    t1 = timeit(lambda: Solution().reverse(x))
    t2 = timeit(lambda: Solution().reverse_v2(x))

    sln = Solution().reverse_v2(x)
    print(sln)
    print("v1:", t1)
    print("v2:", t2)


if __name__ == "__main__":
    main()
