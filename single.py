class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addHead(self, xNumber):
        newNode = Node(xNumber)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addTail(self, xNumber):
        newNode = Node(xNumber)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def addAfter(self, p, xNumber):
        newNode = Node(xNumber)
        curr = self.head
        while curr:
            if curr.data == p:
                newNode.next = curr.next
                curr.next = newNode
                break
            curr = curr.next

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def deletefromHead(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def deletefromTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        curr = self.head
        while curr.next is not self.tail:
            curr = curr.next
        curr.next = None
        self.tail = curr

    def deletaAfter(self, p):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        curr = self.head
        while curr.data != p and curr.next is not None:
            curr = curr.next
        if curr.next is not None:
            node_delete = curr.next
            curr.next = node_delete.next
            node_delete = None
        if curr.next is None:
            self.tail = curr

    def delete(self, x):
        curr = self.head
        prev = None
        while curr is not None:
            if curr.data == x:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def search(self, x):
        curr = self.head
        index = 0
        while curr is not None:
            if curr.data == x:
                return index
            curr = curr.next
            index += 1
        return -1

    def count(self):
        num = 0
        curr = self.head
        while curr is not None:
            num += 1
            curr = curr.next
        return num

    def deleteIndex(self, i):
        i -= 1
        curr = self.head
        if self.head is None:
            return
        if i == 0:
            self.head = curr.next
        for _ in range(i - 1):
            curr = curr.next
            if curr is None:
                break
        if curr is None or curr.next is None:
            return
        next_ = curr.next.next
        curr.next = next_

    def sort(self):
        if self.head is None:
            return
        else:
            curr = self.head
            while curr is not None:
                index = curr.next
                while index is not None:
                    if curr.data > index.data:
                        temp = curr.data
                        curr.data = index.data
                        index.data = temp
                    index = index.next
                curr = curr.next

    def deleteNode(self, p):
        curr = self.head
        while curr is not None and curr.data != p:
            curr = curr.next
        if curr and curr.next:
            curr.next = curr.next.next
        if curr.next is None:
            self.deletefromTail()

    def toArray(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res

    def merge(self, list1, list2):
        dummy = Node(0)
        tail = dummy
        while True:
            if list1 is None:
                tail.next = list2
                break
            elif list2 is None:
                tail.next = list1
                break
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        return dummy.next

    def addBefore(self, x, p):
        new_node = Node(x)
        curr = self.head
        if curr.data == p:
            self.addHead(x)
        while curr.next and curr.next.data != p:
            curr = curr.next
        if curr.next is None:
            return
        new_node.next = curr.next
        curr.next = new_node

    def attach(self, list1, list2):
        if list1.head is None:
            list1.head = list2.head
        else:
            curr = list1.head
            while curr.next is not None:
                curr = curr.next
            curr.next = list2.head

    def max_(self):
        if self.head is None:
            return None
        max_val = self.head.data
        curr = self.head.next
        while curr:
            if curr.data > max_val:
                max_val = curr.data
            curr = curr.next
        return max_val

    def min_(self):
        if self.head is None:
            return None
        min_val = self.head.data
        curr = self.head.next
        while curr:
            if curr.data < min_val:
                min_val = curr.data
            curr = curr.next
        return min_val

    def sum_(self):
        total = 0
        curr = self.head
        while curr:
            total += curr.data
            curr = curr.next
        return total

    def avg(self):
        total = 0
        count = 0
        curr = self.head
        while curr:
            total += curr.data
            count += 1
            curr = curr.next
        return total / count if count > 0 else None

    def sorted_(self):
        curr = self.head
        while curr.next:
            if curr.data > curr.next.data:
                return 0
            curr = curr.next
        return 1

    def insert(self, x):
        curr = self.head
        new_node = Node(x)
        while curr.next:
            if curr.next.data > new_node.data:
                new_node.next = curr.next
                curr.next = new_node
                break
            curr = curr.next
        if curr.next is None:
            self.addTail(x)

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def same(self, list1, list2):
        while list1 and list2:
            if list1.data != list2.data:
                return False
            list1 = list1.next
            list2 = list2.next
        return list1 == list2


values = [2, 3, 4, 5, 6, 7, 8, 9]
num = LinkedList()
for i in range(len(values)):
    num.addHead(values[i])

num.traverse()
