from timeit import timeit


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, cnt = 0, 0
        sub = ""
        for c in s:
            if c in sub:
                idx = sub.index(c)
                sub = sub[idx + 1:] + c
                cnt = len(sub)
            else:
                sub += c
                cnt += 1
                if cnt > longest:
                    longest = cnt
        return longest

    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        longest, cnt = 0, 0
        sub = ""
        for c in s:
            if c in sub:
                idx = sub.index(c)
                sub = sub[idx + 1:] + c
                cnt -= idx
            else:
                sub += c
                cnt += 1
                if cnt > longest:
                    longest = cnt
        return longest


def main():
    s = "dvdf"
    t1 = timeit(lambda: Solution().lengthOfLongestSubstring(s))
    t2 = timeit(lambda: Solution().lengthOfLongestSubstring_v2(s))
    print("v1:", t1)
    print("v2:", t2)

    sln = Solution().lengthOfLongestSubstring_v2(s)
    print(sln)


if __name__ == "__main__":
    main()
