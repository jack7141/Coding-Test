"""
* Linked List
- 배열을 순차적으로 연결된 공간에 데이터를 나열하는 구조
- 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조이다.


구조
1. 노드: 링크드 리스트의 기본단위
2. 포인터: 각 노드안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간
3. Head: 가정 처음에 위치하는 공간
4. Tail: 가장 마지막에 위치하는 공간

종류
양방향 링크드 리스트: 각 노드가 이전 노드와 다음 노드를 모두 참조
원형 링크드 리스트: 마지막 노드가 처음 노드를 참조하는 방식
"""



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#
#     def append(self, data):
#         if not self.head:
#             self.head = Node(data)
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = Node(data)
#
#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next
#
# linked_list = LinkedList()
# linked_list.append('A')
# linked_list.append('B')
# linked_list.append('C')
#
# linked_list.print_list()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)


    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


linked_list = LinkedList()
linked_list.append('C')
linked_list.append('B')
linked_list.append('H')

linked_list.print()
