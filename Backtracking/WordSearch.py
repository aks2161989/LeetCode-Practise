class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if(
                r < 0 or r >= ROWS
                or
                c < 0 or c >= COLS
                or
                board[r][c] != word[i]
            ):
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, i + 1) 
                or
                dfs(r-1, c, i+1)
                or
                dfs(r, c+1, i+1)
                or
                dfs(r, c-1, i+1)
            )

            board[r][c] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")) 