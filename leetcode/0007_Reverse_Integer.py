class Solution:
    def reverse(self, x: int) -> int:
        rev = str(abs(x))[::-1]
        ans = -int(rev) if x < 0 else int(rev)
        if ans < -(2 ** 31) or ans > (2 ** 31) - 1:
            return 0

        return ans

if __name__ == '__main__':
    inputs = [123, -123, 0, 120]
    for input in inputs:
        ans = Solution().reverse(input)
        print(ans)
        
