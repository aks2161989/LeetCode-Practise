from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # generate a dict with numbers and their frequencies
        freq_dict = Counter(nums) 

        heap = []

        for num, freq in freq_dict.items():
            # heapq implements a min-heap under the hood
            # heappush pushes values while ensuring smallest 
            # value is at the root or at index 0 like in a 
            # min heap
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                # heappop removes the smallest element only
                heapq.heappop(heap)
        
        return [num for freq, num in heap]

if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))
