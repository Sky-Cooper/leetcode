class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        merged_list = ListNode()
        current_node = merged_list

        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next

            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        if list1:
            current_node.next = list1

        if list2:
            current_node.next = list2

        return merged_list.next
