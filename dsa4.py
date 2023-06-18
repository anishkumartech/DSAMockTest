class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        sum = x + y + carry
        carry = sum // 10

        current.next = ListNode(sum % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        current.next = ListNode(carry)

    return dummy.next


# Create the linked lists
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
# Output: [7,0,8]
while result:
    print(result.val, end=" ")
    result = result.next
print()


l1 = ListNode(0)
l2 = ListNode(0)

result = addTwoNumbers(l1, l2)
# Output: [0]
while result:
    print(result.val, end=" ")
    result = result.next
print()



l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

result = addTwoNumbers(l1, l2)
# Output: [8,9,9,9,0,0,0,1]
while result:
    print(result.val, end=" ")
    result = result.next
