'''
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
'''

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        if not root:
            return
        if root.left:
            l_child = root.left
            r_child = root.right
            while(l_child):
                l_child.next = r_child
                l_child = l_child.right
                r_child = r_child.left
            self.connect(root.left)
            self.connect(root.right)
        return

sol = Solution()
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.left.left = TreeLinkNode(4)
root.left.right = TreeLinkNode(5)
root.right = TreeLinkNode(3)
root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)

sol.connect(root)


