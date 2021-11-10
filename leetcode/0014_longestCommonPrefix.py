from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = min(strs)
        b = max(strs)
        ans = ""
        for i, c in enumerate(a):
            if c != b[i]:
                return a[:i]
        return a

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        i=0
        for s in zip(*strs):
            if len(set(s))!=1: break
            i+=1
                
        return strs[0][0:i]

if __name__ == '__main__':
    input = ["flower","flow","flight"]
    ans = Solution().longestCommonPrefix2(input)
    print(ans)
