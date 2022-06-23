# наследуйте этот класс от HashTable или расширьте его методами из HashTable

class PowerSet:

    # ваша реализация хранилища
    def __init__(self):
        self.sz = 1000
        self.step = 200
        self.slots = [None] * self.sz

    def hash_fun(self, value: str) -> int:  #
        # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
        summa = 0
        for va in value:
            summa += ord(va)

        return summa % self.sz

    def seek_slot(self, value: str):  #
        # находит индекс пустого слота для значения
        # если массив полный, увеличиваем в два раза
        if self.size() / self.sz > 0.5:
            self.slots = self.slots + [None] * self.sz
            self.sz *= 2
            self.step *= 2

        # ищем ближайший к индексу хэш функции пустой слот
        index = self.hash_fun(value)
        while True:
            if self.slots[index] is None:
                return index
            index = (index + self.step) % self.sz

    def put(self, value):  #
        # всегда срабатывает
        if self.get(value) is False:
            self.slots[self.seek_slot(value)] = value
            return True
        return False

    def find(self, value):  #
        # находит индекс слота со значением, или None
        index = self.hash_fun(value)
        count = self.sz
        while count > 0:
            if self.slots[index] == value:
                return index
            count -= 1
            index = (index + self.step) % self.sz
        return None

    def size(self) -> int:  #
        # количество элементов в множестве
        count = 0
        for x in self.slots:
            if x is not None:
                count += 1
        return count

    def get(self, value):  #
        # возвращает True если value имеется в множестве, иначе False
        return value in self.slots

    def remove(self, value) -> bool:  #
        # возвращает True если value удалено иначе False
        if self.get(value):
            self.slots[self.find(value)] = None
            return True
        return False

    def intersection(self, set2):  #
        # пересечение текущего множества и set2
        self.result_powerset = PowerSet()
        for _ in range(self.sz):
            v = self.slots[_]
            if v is None:
                continue
            if set2.get(v):
                self.result_powerset.put(v)
        return self.result_powerset

    def union(self, set2):  #
        # объединение текущего множества и set2
        self.result_powerset = PowerSet()
        for _ in range(self.sz):
            self.result_powerset.put(self.slots[_])
        for _ in range(len(set2.slots)):
            self.result_powerset.put(set2.slots[_])
        return self.result_powerset

    def difference(self, set2):  #
        # разница текущего множества и set2
        self.result_powerset = PowerSet()
        for _ in range(self.sz):
            v = self.slots[_]
            if v is None:
                continue
            if set2.get(v) is False:
                self.result_powerset.put(v)
        return self.result_powerset

    def issubset(self, set2):
        # возвращает True, если set2 есть подмножество текущего множества, иначе False
        if self.size() < set2.size():
            return False
        for _ in range(self.sz):
            if set2.slots[_] is None:
                continue
            if self.get(set2.slots[_]) is False:
                return False
        return True
