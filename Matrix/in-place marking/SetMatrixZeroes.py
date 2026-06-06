from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix) #Number of rows
        n = len(matrix[0]) #number of columns

        isFirstRowZero = False
        isFirstColumnZero = False

        # Check if first row has any zeroes
        for j in range(n):
            if matrix[0][j] == 0:
                isFirstRowZero = True
                break

        # Check if first column has any zeroes
        for i in range(m):
            if matrix[i][0] == 0:
                isFirstColumnZero = True
                break

        #If an inner cell is 0 mark its first row and column to 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        ''' Using the above markers set remaining inner row and 
        column elements to 0'''
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # If required, set first row and/or first column to 0
        if isFirstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        if isFirstColumnZero:
            for i in range(m):
                matrix[i][0] = 0

if __name__ == "__main__":
    sol = Solution()
    matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
    sol.setZeroes(matrix)
    print(matrix)


        