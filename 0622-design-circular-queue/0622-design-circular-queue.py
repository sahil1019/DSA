class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.k = k
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k