from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            group[key].append(s)
            
        return list(group.values())
    
if __name__ == "__main__":
    Sol = Solution()
    print(Sol.groupAnagrams(["eat", "eat", "tea"]))

