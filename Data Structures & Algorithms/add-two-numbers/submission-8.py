# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sumAndCarry = lambda x,y,c = 0 : (x+y+c, 0) if x+y+c < 10 else ((x+y+c)%10, 1)

        digit, carry = sumAndCarry(l1.val, l2.val) 
        new_head = ListNode(digit)
        current = new_head
        l1 = l1.next
        l2 = l2.next
        while l1 or l2 or carry:

            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            digit, carry = sumAndCarry(value1, value2, carry)
            current.next = ListNode(digit) 
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return new_head

        