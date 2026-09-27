class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        missing  = n

        for i in range(n):
            missing ^= i
            missing ^= nums[i]

        return missing

sol = Solution()
print(sol.missingNumber([0,1]))