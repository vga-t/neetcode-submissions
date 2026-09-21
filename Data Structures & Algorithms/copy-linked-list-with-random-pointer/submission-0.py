"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        old2new = {None:None}
        dummy = Node(0)
        new_current = dummy
        while current:
            new_current.next = old2new.setdefault(current, Node(current.val))
            if current.random in old2new:
                new_current.next.random = old2new[current.random]
            else:
                old2new[current.random] = Node(current.random.val)
                new_current.next.random = old2new[current.random]

            new_current = new_current.next
            current = current.next

        new_current.next = None
        
        return dummy.next


                


