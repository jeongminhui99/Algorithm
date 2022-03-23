# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val) :
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1
    
    
    # list1 : l1 -> 1 -> 2 -> 4
    # list2 : l2 -> 1 -> 3 -> 4
    
   
    #     l1
    # 1 -> 2 -> 4
    # l2 -> 1 -> 3 -> 4
    
    #     l2
    # 1 -> 2 -> 4
    # l1 -> 1 -> 3 -> 4
    
    # res : 1 -> 1 -> 3 -> 4 
    
    
    #     l1
    # 1 -> 3 -> 4
    # l2 -> 2 -> 4
    
    #     l2
    # 1 -> 3 -> 4
    # l1 -> 2 -> 4
    
    # res : 1 -> 1 -> 2 -> 4 
    
    
    #     l1
    # 2 -> 4
    # l2 -> 3 -> 4
    
    #     l2
    # 2 -> 4
    # l1 -> 3 -> 4
    
    # res : 1 -> 1 -> 2 -> 3 -> 4
    
    
    
    #     l1
    # 3 -> 4
    # l2 -> 4
    
    # mergeTwoLists(None, list2)
    # l2 -> None
    # l1 -> 4
    
    # res : 1 -> 1 -> 2 -> 3 -> 4 -> 4