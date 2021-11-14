from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map: dict[tuple[str]] = {}
        for s in strs:
            sorted_str = tuple(sorted(list(s)))
            if hash_map.get(sorted_str):
                hash_map[sorted_str].append(s)
            else:
                hash_map[sorted_str] = [s]
        
        return [item for item in hash_map.values()]

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    ans = Solution().groupAnagrams(strs)
    print(ans)
