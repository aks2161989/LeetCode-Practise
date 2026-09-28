from typing import List

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(r, c, reachable):
            reachable.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if(0 <= nr < rows and
                   0 <= nc < cols and
                   (nr, nc) not in reachable and
                   heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)
            
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)

        result = []

        for r in range(rows):
            for c in range(cols):
                if(r, c) in pacific and (r,c) in atlantic:
                    result.append([r,c])

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))


        