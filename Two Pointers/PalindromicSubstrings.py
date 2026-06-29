class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand_from_center(left, right):
            palindromes_found = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromes_found += 1
                left -= 1
                right += 1
            return palindromes_found
        
        for i in range(len(s)):
            count += expand_from_center(i, i)
            count += expand_from_center(i, i+1)
        
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("aaa"))
