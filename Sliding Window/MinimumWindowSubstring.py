from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        best_len = float("inf")
        best_start = 0
        left = 0
        right = 0

        if n > m:
            return ""

        need = Counter(t)
        window = defaultdict(int)
        formed = 0
        required = len(need)

        for right in range(m):

            right_char = s[right]
            window[right_char] += 1
            
            if right_char in need and window[right_char] == need[right_char]:
                formed += 1

            while formed == required:
                current_window_len = right - left + 1

                if current_window_len < best_len:
                    best_len = current_window_len
                    best_start = left

                left_char = s[left]

                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                
                left += 1
            
        
        if best_len == float("inf"):
            return ""
        
        return s[best_start: best_start + best_len]

if __name__ == "__main__":
    sol = Solution()
    result = sol.minWindow(s = "a", t = "aa")
    print(result if result else "Empty string")
                
