class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head: ListNode) -> ListNode:
    slow = fast = entry = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            while slow != entry:
                slow = slow.next
                entry = entry.next
            return entry

    return None


def hasCycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    ptA = headA
    ptB = headB

    while ptA != ptB:
        ptA = ptA.next if ptA else headB
        ptB = ptB.next if ptB else headA

    return ptA


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    ptDelayed = ptCur = head
    i = 0
    while ptCur:
        if i > n:
            ptDelayed = ptDelayed.next
        ptCur = ptCur.next
        i += 1

    if i == n:
        head = head.next
    else:
        ptDelayed.next = ptDelayed.next.next
    return head
