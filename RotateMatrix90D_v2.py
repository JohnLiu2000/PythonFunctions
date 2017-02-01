## running time 46ms
## Java could achieve it much faster with time of 3ms

import copy

class Solution():
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ## This outputs Arithmetic of the set and subset

        # n X m is the dimension of the matrix
        temp = copy.deepcopy(matrix)
        n = len(temp)

        for i in range(n):
            for j in range(n):
                matrix[j][i] = temp[n-1-i][j]

            
    
matrix = [[1,2], [3,4]]
print(matrix)

# define a new object
s = Solution()
s.rotate(matrix)
print(matrix)
