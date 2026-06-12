class LFUCache:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.freq = 1
            self.prev = None
            self.next = None

    class DLL:
        def __init__(self):
            self.head = LFUCache.Node(0, 0)
            self.tail = LFUCache.Node(0, 0)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0

        def add(self, node):
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.size += 1

        def remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1

        def pop(self):
            if self.size == 0:
                return None
            node = self.tail.prev
            self.remove(node)
            return node

    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.nodes = {}
        self.freqs = {}

    def update(self, node):
        freq = node.freq
        self.freqs[freq].remove(node)

        if freq == self.min_freq and self.freqs[freq].size == 0:
            self.min_freq += 1

        node.freq += 1
        self.freqs.setdefault(node.freq, self.DLL()).add(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.update(node)
            return

        if len(self.nodes) == self.cap:
            node = self.freqs[self.min_freq].pop()
            del self.nodes[node.key]

        node = self.Node(key, value)
        self.nodes[key] = node
        self.min_freq = 1
        self.freqs.setdefault(1, self.DLL()).add(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)