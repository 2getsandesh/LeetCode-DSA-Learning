'''Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
 Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
   Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
                head=head.next
        return False
    
#---------------------------Two Pointer--------------------------------#

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = fast = head
            while fast.next:
                slow = slow.next
                fast = fast.next.next
                if fast == slow: return True

        except: return False