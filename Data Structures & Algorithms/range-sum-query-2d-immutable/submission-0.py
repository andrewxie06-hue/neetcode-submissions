class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.__matrix = []
        
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                if j == 0:
                    row.append(matrix[i][j])
                    continue
                row.append(row[j-1] + matrix[i][j])
            self.__matrix.append(row)

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
       
        for i in range(row1, row2 + 1):
            print(i)
            sum += self.__matrix[i][col2]
            if col1 > 0:
                sum -= self.__matrix[i][col1-1]
        
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)