from collections import deque

# 1->2->3->4->4->3->2->1
# b  b  b  b
# f     f     f     b 
# 1->2->3->4->5->4->3->2->1
# b  b  b  b  b
# f     f     f     f     f
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    arr = []
    def isPalindrome(self, head: ListNode) -> bool:
        stack = deque()
        if (head == None):
            return False
        if (head.next == None):
            return True
        back = head
        front = head
        if(head.next.next == None):
            if(head.val == head.next.val):
                return True
            else:
                return False
        #store all values till mid in linked list to a stack
        while (front.next != None and front.next.next !=  None):
            stack.append(back.val)
            back = back.next
            front = front.next.next
        if(front.next == None):
            back = back.next
        else:
            temp = back.val
            if(back.next.val != temp):
                return False
            back = back.next.next
        while (back != None):
            poppedval = stack.pop()
            if back.val != poppedval :
                return False
            back = back.next
        return True
            