class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b!= 0:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        if a <= MAX_INT:
            return a

        return ~(a ^ MASK)

if __name__ == "__main__":
    sol =Solution()
    print(sol.getSum(5, 3)) 