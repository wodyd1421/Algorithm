class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = dict()
        for i in range(len(grid)):
            columns[i+1] = list()
            for j in range(len(grid)):
                columns[i+1].append(grid[j][i])
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if columns[i+1] == grid[j]:
                    output += 1
        return output