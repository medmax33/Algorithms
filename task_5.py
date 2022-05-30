class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)
        return None

    def dequeue(self):
        if self.size() != 0:
            return self.queue.pop()
        return None

    def size(self):
        return len(self.queue)
