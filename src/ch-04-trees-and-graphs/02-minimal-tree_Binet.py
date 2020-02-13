##Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

##For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
      ##These binary sort tree problems always have a left, middle, right
      ##Based on the return above, you can make a new TreeNode, and pass its value, and that will act as the root
      ##YMU by not remembering when you do [:] that you DONT TAKE IN LAST VALUE
      ##but you DO TAKE IN FIRST VALUE
      ##YMU by not doing the base case of no nums, should do that
      if not nums:
          return None
      ln = len(nums)
      ##this sets cur_node value
      cur_node = TreeNode(nums[ln//2])
      cur_node.left = self.sortedArrayToBST(nums[:ln//2])
      cur_node.right = self.sortedArrayToBST(nums[ln//2+1:])
      ##Return node result with set side nodes
      return cur_node

