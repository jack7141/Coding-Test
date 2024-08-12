

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data=data)

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            # insert할 노드의 바로앞을 찾는다
            # 그러면서 하나씩 옮겨 담음
            for _ in range(position - 1):
                if current:
                    current = current.next
            new_node.next = current.next  # 새 노드의 다음 노드를 삽입 위치의 노드로 지정
            current.next = new_node  # 삽입 위치의 앞 노드의 다음 노드를 새 노드로 지정

    def delete(self, data):  # 주어진 값을 가진 노드를 리스트에서 삭제
        if self.head and self.head.data == data:  # 삭제할 노드가 head 노드인 경우
            self.head = self.head.next  # head 노드를 다음 노드로 지정
        else:
            current = self.head
            while current and current.next and current.next.data != data:  # 삭제할 노드를 찾는 루프
                current = current.next
            if current and current.next:  # 삭제할 노드를 찾은 경우
                current.next = current.next.next  # 삭제할 노드 앞의 노드의 다음 노드를 삭제할 노드의 다음 노드로 지정