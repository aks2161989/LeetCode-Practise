from typing import List, Set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if num-1 not in numsSet:
                current_num = num
                current_length = 1

                while current_num+1 in numsSet:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)
        
        return longest
    
if __name__ == "__main__":
    Sol = Solution()
    result = Sol.longestConsecutive([100,4,200,1,3,2])
    print(result)
    result = Sol.longestConsecutive([100])
    print(result)    