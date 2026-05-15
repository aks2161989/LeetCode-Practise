from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False
    
if __name__ == "__main__":
    Sol = Solution()
    result = Sol.containsDuplicate([1,2,3,4])
    print(result)
    result = Sol.containsDuplicate([1])
    print(result)
    result = Sol.containsDuplicate([1,1])
    print(result)