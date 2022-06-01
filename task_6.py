class Deque:
    def __init__(self):
        self.dequ = []

    def addFront(self, item):
        # добавление в голову - слева
        self.dequ.insert(0, item)

    def addTail(self, item):
        # добавление в хвост - справа
        self.dequ.append(item)

    def removeFront(self):
        # удаление из головы  - слева
        if self.size() != 0:
            return self.dequ.pop(0)
        return None  # если очередь пуста

    def removeTail(self):
        # удаление из хвоста  - справа
        if self.size() != 0:
            return self.dequ.pop()
        return None  # если очередь пуста

    def size(self):
        return len(self.dequ)  # размер очереди

    def into(self, item):
        for i in self.dequ:
            if i == item:
                return True
        return False


def palindrom(s: str) -> bool:
    pal = Deque()
    for letter in s:
        if letter != ' ':
            pal.addFront(letter.lower())

    while pal.size() > 1:
        f = pal.removeFront()
        t = pal.removeTail()
        if f != t:
            return False

    return True
