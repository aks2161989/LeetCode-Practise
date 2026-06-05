from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        '''
        First pass: Here multiply each element in answers with
        the product of the prefixes of the equivalent element 
        in nums
        ''' 
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        '''
        Second pass: Here multiply each element in answers with 
        the product of the suffixes of the equivalent element
        from nums 
        '''
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))