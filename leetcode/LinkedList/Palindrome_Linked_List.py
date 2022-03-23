# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        # 데크 자료형 선언
        q: Deque = collections.deque()
        
        #리스트 변환
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 팰린드롬 판별
        while len(q)>1 :
            if q.popleft() != q.pop():
                return False
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        rev = None
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # 홀수인 경우 중앙값 배제를 위해
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
            
        return not rev