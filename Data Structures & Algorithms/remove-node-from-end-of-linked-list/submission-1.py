# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        target = length - n
        print(target)
        


        if target == 0:
            head = head.next
            return head
        index = 1
        prev = head
        current = head.next
        while current:

            if target == index:
                prev.next = current.next
                print(current.val)
                return head

            prev = current
            current = current.next
            index += 1
