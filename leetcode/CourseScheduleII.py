'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
Hints:

This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
'''
import collections

class Solution:
    def findOrder(self, numCourses, prerequisites):
        incoming_adj_list = collections.defaultdict(set)
        adj_list = collections.defaultdict(set)
        for i,j in prerequisites:
            incoming_adj_list[i].add(j)
            adj_list[j].add(i)
        stack = [i for i in range(numCourses) if not incoming_adj_list[i]]
        course_list = []
        
        while(stack):
            v = stack.pop()
            course_list.append(v)
            for neighbor in adj_list[v]:
                incoming_adj_list[neighbor].remove(v)
                if not incoming_adj_list[neighbor]:
                    stack.append(neighbor)
            incoming_adj_list.pop(v)
        if not incoming_adj_list:
            return course_list
        else:
            return []
        




            
sol = Solution()

edge_list = [[1,0], [0,2], [1,2]]
print(f'Input: {3}, {edge_list}')
print(f'Output: {sol.findOrder(3, edge_list)}')
