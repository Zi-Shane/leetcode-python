class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]

if __name__ == '__main__':
    x = 12345654321
    ans = Solution().isPalindrome(x)
    print(ans)
