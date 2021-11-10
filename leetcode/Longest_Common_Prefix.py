class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s2[:i]
        return s1


strs = ["flower","flow","fliwht"]
# strs = ["dog","racecar","car"]

sol = Solution()
print(sol.longestCommonPrefix(strs))

