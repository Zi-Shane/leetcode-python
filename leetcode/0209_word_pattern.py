class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        char_word_map_a = {}
        char_word_map_b = {}
        for i in range(len(pattern)):
            if pattern[i] not in char_word_map_a:
                char_word_map_a[pattern[i]] = words[i]
            elif char_word_map_a[pattern[i]] != words[i]:
                return False
            if words[i] not in char_word_map_b:
                char_word_map_b[words[i]] = pattern[i]
            elif char_word_map_b[words[i]] != pattern[i]:
                return False
        
        return True
    
    def wordPattern2(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        d = zip(pattern, words)
        # print(set(d))
        # print(set(pattern))
        # print(set(words))
        return len(set(d)) == len(set(pattern)) == len(set(words))
        
    def wordPattern3(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        d = {}
        for i in range(len(pattern)):
            a, b = pattern[i], words[i]
            if a not in d:
                if b not in d.values():
                    d[a] = b
                else:
                    return False
            elif d[a] != b:
                    return False
        
        return True

if __name__ == '__main__':
    inputs = [("abba", "dog cat cat dog"), ("abba", "dog cat cat fish"), ("abba", "dog dog dog dog"), ("aaa", "aa aa aa aa")]
    s = "dog cat cat dog"
    sol = Solution()
    for pattern, s in inputs:
        # ans = sol.wordPattern(pattern, s)
        ans = sol.wordPattern2(pattern, s)
        # ans = sol.wordPattern3(pattern, s)
        print(ans)
        
