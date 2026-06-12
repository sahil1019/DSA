class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node(0)  # dummy head
        self.tail = Node(0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_to_node = {}

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            if self.head.next == self.tail or self.head.next.count > 1:
                new_node = Node(1)
                self._insert_after(self.head, new_node)

            self.head.next.keys.add(key)
            self.key_to_node[key] = self.head.next

        else:
            curr = self.key_to_node[key]
            nxt = curr.next

            if nxt == self.tail or nxt.count != curr.count + 1:
                nxt = Node(curr.count + 1)
                self._insert_after(curr, nxt)

            nxt.keys.add(key)
            self.key_to_node[key] = nxt

            curr.keys.remove(key)
            if not curr.keys:
                self._remove(curr)

    def dec(self, key: str) -> None:
        curr = self.key_to_node[key]

        if curr.count == 1:
            del self.key_to_node[key]
        else:
            prev = curr.prev

            if prev == self.head or prev.count != curr.count - 1:
                node = Node(curr.count - 1)
                self._insert_after(prev, node)
                prev = node

            prev.keys.add(key)
            self.key_to_node[key] = prev

        curr.keys.remove(key)
        if not curr.keys:
            self._remove(curr)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))