'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''

class Solution:
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0
        counts = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            counts[0][i] = 1
        for i in range(n):
            counts[i][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                counts[i][j] = counts[i-1][j] + counts[i][j-1]

        return counts[n-1][m-1]

sol = Solution()
m = 7
n = 3
print(f'Input: m = {m}, n = {n}')
print(f'Output: {sol.uniquePaths(m,n)}')
