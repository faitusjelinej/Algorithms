def maximalSquare(matrix):
    area = 0
    if matrix:
        prev = [0]*len(matrix[0])
        for row in matrix:
            current = [1 if ch == '1' else 0 for ch in row]
            for j in range(1,len(current)):
                if current[j]:
                    current[j] = min(prev[j-1],prev[j],current[j-1])+1
            area = max(area,max(current)**2)
            prev = current
    return area


matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

print(maximalSquare(matrix))
