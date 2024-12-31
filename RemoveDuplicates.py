# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the 'head' of a sorted linked list, delete all duplicates such that 
        each element appears only once.
        
        Return the linked list sorted as well
        """
        output = []
        listNode = head[0]
        if listNode.next is None:
            return [listNode.val]
        current = listNode
        while (current is not None):
            output.append(current.val)
            while current.val == current.next.val:
                current.next = current.next.next
            current = current.next

        return output


        


        """
        Constraints:

            # The number of nodes in the list is in the range [0, 300].
            # -100 <= Node.val <= 100
            # The list is guaranteed to be sorted in ascending order.
        """