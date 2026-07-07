"""
Definition of Interval:
"""
import heapq
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x.start)

        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, interval.end)
        
        return len(min_heap)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minMeetingRooms([Interval(0,40),Interval(5,10),Interval(15,20)]))
    