class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        columns_new = len(matrix)
        rows_new = len(matrix[0])
        for i in range(rows_new):
            result.append([])
        for x in range(columns_new):
            for y in range(rows_new):
                result[y].append(matrix[x][y])
        return result