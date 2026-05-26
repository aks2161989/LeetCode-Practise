from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i

if __name__ == "__main__":
    Sol = Solution()
    print(Sol.twoSum([0, 4, 3, 0], 0))