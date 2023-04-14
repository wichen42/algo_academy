# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1.next
            l1 = l1.next
        else:
            tail.next = l2.next
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    else: 
        tail.next = l2
    
    return dummy.next

def recursiveMergeTwoLists(l1, l2):
    if l1 == None: return l2
    if l2 == None: return l1
    
    if l1.val < l2.val:
        next1 = list1.next
        l1.next = self.recursiveMergeTwoLists(next1, l2)
        return l1
    else:
        next2 = l2.next
        l2.next = self.recursiveMergeTwoLists(l1, next2)
        return l2