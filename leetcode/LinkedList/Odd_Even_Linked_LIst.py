# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next #마지막 홀수 짝수 연결을 위한 포인터
        
        while even and even.next:
            # odd.next, odd = odd.next.next, odd.next
            # 이런 형태는 안됨 odd가 3이 아니라 2가 된다.
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
            
        odd.next = even_head
        return head
    
    #odd. even, even_head 변수들은 n의 크기에 상관없이 일정하게 유지 -> 공간복잡도 O(1)