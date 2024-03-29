'''
1047. Remove All Adjacent Duplicates In String
Easy

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

 

Note:

    1 <= S.length <= 20000
    S consists only of English lowercase letters.
'''


class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) < 2:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return ''
            else:
                return s

        i = 0
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                i = max(0, i - 1)
            else:
                i += 1

        return s


sol = Solution()
s = 'abbaca'
print(sol.removeDuplicates(s))
