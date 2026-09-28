# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while True:
            # Check if k nodes are available
            kth = prev

            for i in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            group_next = kth.next

            # Reverse the current group
            curr = prev.next
            prev_node = group_next

            while curr != group_next:
                nxt = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = nxt

            # Connect the reversed group
            temp = prev.next
            prev.next = kth
            prev = temp