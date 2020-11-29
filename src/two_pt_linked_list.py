class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle(head: ListNode) -> ListNode:
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


def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    ptA = headA
    ptB = headB

    while ptA != ptB:
        ptA = ptA.next if ptA else headB
        ptB = ptB.next if ptB else headA

    return ptA


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
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


def rotate_right(head: ListNode, k: int) -> ListNode:
    # empty list case
    if not head:
        return head
    # one element case
    if not head.next:
        return head

    prev_tail = head
    n = 1
    while prev_tail.next:
        prev_tail = prev_tail.next
        n += 1

    prev_tail.next = head
    new_tail = head

    tail_idx = (n - k % n - 1)
    for i in range(0, tail_idx):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head
