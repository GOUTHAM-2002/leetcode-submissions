class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Transpose the matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                #this seems important
                if col > row: 
                    matrix[row][col],matrix[col][row] = matrix[col][row], matrix[row][col]
        #Flip the columns of the matrix
        for row in range(len(matrix)):
            matrix[row].reverse()
    