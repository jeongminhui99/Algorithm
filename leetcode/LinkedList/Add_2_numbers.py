# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 연결 리스트 뒤집기
    def reverse(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinked(serlf, result: str) -> ListNode:
        prev: ListNode = None

        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
            
        return node
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        # 두 연결 리스트의 덧셈
        a = self.toList(self.reverse(l1))
        b = self.toList(self.reverse(l2))
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.toReversedLinked(str(resultStr))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # 몫(자리올림수)과 나머지(값) 계산
            # divmod : (a//b, a%b)
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
            
        return root.next