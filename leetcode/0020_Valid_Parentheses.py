class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pa = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if pa.get(c) == None:
                stack.append(c)
            elif len(stack) > 0:
                if pa.get(c) != stack.pop():
                    return False
            else:
                return False
        
        return stack == []
        
if __name__ == '__main__':
    inputs = ["{[]}", "([)]", "[", "]"]
    sol = Solution()
    for input in inputs:
        ans = sol.isValid(input)
        print(ans)
