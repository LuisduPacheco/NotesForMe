#Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
     

class Solution:
  def deleteNode(self, node: ListNode):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    newVal = node.next.val
    newNext = node.next.next

    node.val = newVal
    node.next = newNext





