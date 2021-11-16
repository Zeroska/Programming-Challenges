 class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:   
    if head is not None:
        if head.val == val:
            head = head.next

    while head is not None:
        # Store the head
        temp = head
        nextNode = head.next
        if temp.val == val:
            head = nextNode

        if nextNode.val == val:
            head.next = nextNode.next
            nextNode.next = None

        # Update the head to traverse forward
        head = head.next
            


def main(): 
    a = ListNode(1)
    a.next = b
    b = ListNode(2)
    b.next = c
    c = ListNode(3)
    c.next = d
    d = ListNode(4)

    removeElements()


if if __name__ == '__main__':
    main()

    