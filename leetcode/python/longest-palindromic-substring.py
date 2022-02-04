# [problem:longest-palindromic-substring](https://leetcode.com/problems/longest-palindromic-substring)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longestPalindromeByPosition(s: str, l: int, r: int, res_cache: str) -> str:
            res = res_cache
            while (l >= 0) and (r < len(s)):  # odd case
                if s[l] == s[r]:
                    if len(res) < (r - l) + 1:
                        res = s[l:r + 1]
                    l = l - 1
                    r = r + 1
                else:
                    break
            return res

        res = ""
        for i in range(len(s)):
            res = longestPalindromeByPosition(s, i, i, res)
            res = longestPalindromeByPosition(s, i, i+1, res)
        return res

def test(given, expected):
    inst = Solution()
    actual = inst.longestPalindrome(given)
    assert actual == expected, f"Test failed for input: {given}, expected: {expected} but actual: {actual}"
    print(f"Test pass for input: {given}, actual: {actual}")

test("babad", "bab")
test("cbdd", "dd")
test("a", "a")
test("abcd", "a")
test("abb", "bb")
test("aaaa", "aaaa")
test("aacabdkacaa", "aca")
