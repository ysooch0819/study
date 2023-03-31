# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(-1)
        cursor = head
        print(cursor.val)
        print(cursor.next)

        while list1!=None and list2!=None:
            if list1.val <= list2.val:
                cursor.next=list1
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next
            cursor = cursor.next

        cursor.next = list1 if list1 != None else list2

        return head.next