class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in matching:
                if not stack or stack[-1] != matching[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(s = "([)]"))                           