from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
            """
            Do not return anything, modify s in-place instead.
            """
            l = len(s) // 2
            while l < len(s):
                s[l], s[~l] = s[~l], s[l]
                l += 1
            

if __name__ == '__main__':
    input = ["h","e","l","l","o"]
    Solution().reverseString(input)
    print(input)
