class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result <<= 1

            rightmost = n & 1

            result |= rightmost

            n >>= 1

        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(2147483644))