class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map_s = {}
        char_map_t = {}
        for i in range(len(s)):
            if char_map_s.get(s[i]) == None:
                char_map_s[s[i]] = t[i]
            elif char_map_s.get(s[i]) != t[i]:
                return False
            
            if char_map_t.get(t[i]) == None:
                char_map_t[t[i]] = s[i]
            elif char_map_t.get(t[i]) != s[i]:
                return False
        
        return True
        
        
if __name__ == '__main__':
    inputs = [("egg", "add"), ("foo", "bar"), ("paper", "title"), ("badc", "baba")]
    for s, t in inputs:
        ans = Solution().isIsomorphic(s, t)
        print(ans)
    