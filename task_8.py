class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str) -> int:
        # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
        summa = 0
        for va in value:
            summa += ord(va)

        return summa % self.size

    def seek_slot(self, value: str):
        # находит индекс пустого слота для значения, или None
        index = self.hash_fun(value)
        count = self.size
        while count > 0:
            if self.slots[index] is None:
                return index
            count -= 1
            index = (index + self.step) % self.size
        return None

    def put(self, value):
        # записываем значение по хэш-функции возвращается индекс
        # слота или None, если из-за коллизий элемент не удаётся
        # разместить
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
            return index
        return None

    def find(self, value):
        # находит индекс слота со значением, или None
        index = self.hash_fun(value)
        count = self.size
        while count > 0:
            if self.slots[index] == value:
                return index
            count -= 1
            index = (index + self.step) % self.size
        return None
