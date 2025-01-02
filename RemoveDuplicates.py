from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(val=1, next=None)
b = ListNode(val=10, next=None)
c = ListNode(val=1, next=None)
d = ListNode(val=-101, next=None)
e = ListNode(val=2, next=None)
f = ListNode(val=3, next=None)
g = ListNode(val=3, next=None)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the 'head' of a sorted linked list, delete all duplicates such that 
        each element appears only once.
        
        Return the linked list sorted as well
        """

        # Assert the constraints
        self.assertConstraints(head)

        if head.next is None:
            return head

        current = head
        while (current is not None):
            while current.next is not None and current.val == current.next.val:
                current.next = current.next.next
            current = current.next

        return head


    def printResult(self, head:Optional[ListNode]):
        
        current = head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")




    def assertConstraints(self, head: Optional[ListNode]):
        """
        Constraints:
        # The number of nodes in the list is in the range [0, 300].
        # -100 <= Node.val <= 100
        # The list is guaranteed to be sorted in ascending order.
        """
        # Ensure the list size is within [0, 300]
        count = 0
        current = head
        while current is not None:
            count += 1
            assert -100 <= current.val <= 100, f"Node value {current.val} is out of bounds (-100 to 100)"
            if current.next is not None:
                assert current.val <= current.next.val, f"List is not sorted: {current.val} > {current.next.val}"
            current = current.next
        assert 0 <= count <= 300, f"Number of nodes {count} is out of bounds (0 to 300)"


        
solution = Solution()
output = solution.deleteDuplicates(a)
solution.printResult(output)

