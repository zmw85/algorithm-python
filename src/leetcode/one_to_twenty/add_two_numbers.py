from src.data_structure.binary_tree.link_list import ListNode


def solution_1(l1, l2):
    if not l1 or not l2:
        return None

    str1 = str2 = ''

    temp = l1
    while temp:
        str1 = str(temp.val) + str1
        temp = temp.next

    temp = l2
    while temp:
        str2 = str(temp.val) + str2
        temp = temp.next

    output = temp = None
    sum = int(str1) + int(str2)
    for c in str(sum)[::-1]:
        if temp is None:
            output = temp = ListNode(c)
        else:
            temp.next = ListNode(c)
            temp = temp.next

    return output


def solution_2(l1, l2):
    if not l1 or not l2:
        return None

    output = ListNode(0)
    current = None
    carry = 0

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum = val1 + val2 + carry

        carry = sum // 10
        current.next = ListNode(sum % 10 if carry else sum)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        current.next = ListNode(1)

    return output.next
