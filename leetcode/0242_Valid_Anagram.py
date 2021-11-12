from typing import AnyStr


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        for a, b in zip(s, t):
            if hash_map.get(a) == None:
                hash_map[a] = 1
            else:
                hash_map[a] += 1
            if hash_map.get(b) == None:
                hash_map[b] = -1
            else:
                hash_map[b] -= 1
        
        for i in hash_map:
            if hash_map.get(i) == None or hash_map.get(i) != 0:
                return False

        return True

if __name__ == '__main__':
    inputs_s = ["anagram", "rat", "aacc"]
    inputs_t = ["nagaram", "car", "ccac"]
    for i in range(len(inputs_s)):
        ans = Solution().isAnagram(inputs_s[i], inputs_t[i])
        print(ans)
