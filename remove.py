class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removekthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #Make 2 pointers called prev and curr.
	#Initialize both pointer to start at the head.
	#Also we need a counter to know how made nodes the curr
	#has traversed ahead.
        counter = 1
        prev = head
        curr = head
        if head.next is None:
            return head
        while counter <= n:
            curr = curr.next
            counter += 1
	#First check to see if the curr pointer is already at None.
	#That means the prev pointer is already sitting at the node
	#that needs to be removed. If so,
	#we re-assign the value of the head of the node to be the next
	#node after it and then have it point to next value of of the next
	#node
        if curr is None:
            head.val = head.next.val
            head.next = head.next.next
            return
        while curr.next is not None:
            curr = curr.next
            prev = prev.next
        #prev is pointing to the node right before the node we want to remove
        #prev.next = Node_To_Remove
        prev.next = prev.next.next
        return head
