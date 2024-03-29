'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''

class Solution:
    def judgeCircle(self, moves):
        dic = {'U':0, 'D':0, 'L':0, 'R':0}
        for s in moves:
            dic[s] += 1
        if (dic['U'] == dic['D']) and (dic['L'] == dic['R']):
            return True
        else:
            return False

sol = Solution()
moves = 'UD'
print(f'Input: {moves}')
print(f'Output: {sol.judgeCircle(moves)}')

moves = 'LL'
print(f'Input: {moves}')
print(f'Output: {sol.judgeCircle(moves)}')
