class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 만약 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            # self.table[index] is None 이 아닌 이유 
            # => 존재하지 않는 인덱스로 조회를 시도할 경우 바로 디폴트 객체 생성 즉,  빈 ListNode 생성
            # => self.table[index] is None이 절대로 True가 되지 않는 버그 발생
            self.table[index] = ListNode(key, value)
            return 
        
        # 만약 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return 
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p=p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        p = self.table[index]
        if p.key == key:
            # defauldict이기 때문에 None으로 할당한다면 self.table[index] is None에서 오류
            self.table[index] = ListNode() if p.next is None else p.next
            return
        prev = p
        while p :
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next