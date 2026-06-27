from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        answer = []

        while left<=right and top<=bottom:
            for col in range(left, right+1):
                answer.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                answer.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    answer.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top-1, -1):
                    answer.append(matrix[row][left])  
                left += 1  
        
        return answer

if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
