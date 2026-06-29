class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        max_length = 0
        left = 0
        right = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])
            current_window_length = right - left + 1

            if (current_window_length) - max_freq > k:
                char = s[left]
                freq[char] -= 1
                left += 1

            max_length = max(max_length, right - left + 1) 
        
        return max_length

if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement(s = "AABABBA", k = 1))