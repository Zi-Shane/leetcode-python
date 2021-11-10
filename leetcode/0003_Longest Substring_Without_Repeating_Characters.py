class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        l_index = 0
        r_index = 0
        tmp = 0
        count = 0
        hash_table = {}
        
        while r_index < len(s):
            ch = s[r_index]
            if ch in hash_table and hash_table[ch] >= l_index:
                tmp = r_index - l_index  # current length
                l_index = hash_table[ch] + 1
                hash_table[ch] = r_index
            else:
                hash_table[ch] = r_index
                if r_index == len(s) - 1:
                    tmp = r_index - l_index + 1  # the last char in string
            
            # update longest substring counter
            if tmp > count:
                count = tmp
            
            r_index += 1
            
        return count
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        my_str = ""
        max_len = 0
        for c in s:
            if c in my_str:
                my_str = my_str[my_str.find(c) + 1:]
            my_str += c
            max_len = max(len(my_str), max_len)
        
        return max_len

if __name__ == '__main__':
    inputs = ["abcabcbb", "bbbbb", "pwwkew", "tmmzuxt", " ", "cdd"]

    for input in inputs:
        print("input: ", input)
        ans = Solution().lengthOfLongestSubstring1(input)
        print("lengthOfLongestSubstring1() answer: ", ans)
        
        ans = Solution().lengthOfLongestSubstring2(input)
        print("lengthOfLongestSubstring2() answer: ", ans)
        
        print("--------------")
        

