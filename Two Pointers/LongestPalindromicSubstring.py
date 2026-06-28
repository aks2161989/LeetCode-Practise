class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1: right]
        
        for i in range(len(s)):
            odd_palindrome = expand_from_center(i, i)
            even_palindrome = expand_from_center(i, i+1)

            if len(odd_palindrome) > len(result):
                result = odd_palindrome

            if len(even_palindrome) > len(result):
                result = even_palindrome
        
        return result
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("bb"))