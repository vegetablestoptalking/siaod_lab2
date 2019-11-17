class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class RingList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            self.length += 1
        else:
            cur = self.head
            new_item = Node(data)
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_item
            new_item.next = self.head
            self.length += 1

    def find(self, data):
        cur = self.head
        while cur:
            if data == cur.data:
                return True
            if self.head == cur.next:
                break
            cur = cur.next
        return False

    def __str__(self):
        result = '['
        cur = self.head
        while cur:
            result += str(cur.data) + ', '
            cur = cur.next
            if cur == self.head:
                break
        result = result[0:-2]
        result += ']'
        return result

    def __getitem__(self, key):
        length = 0
        cur1 = None
        cur = self.head
        while key != length and cur.next != self.head:
            cur = cur.next
            length += 1
        if key == length:
            cur1 = cur.data
        return cur1

    def __len__(self):
        return self.length








