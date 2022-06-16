# наследуйте этот класс от HashTable или расширьте его методами из HashTable

class PowerSet:

    # ваша реализация хранилища
    def __init__(self):
        self.slots = []

    def size(self) -> int:  #
        # количество элементов в множестве
        return len(self.slots)

    def put(self, value):  #
        # всегда срабатывает
        if self.get(value) is False:
            self.slots.append(value)
            return True
        return False

    def get(self, value):  #
        # возвращает True если value имеется в множестве, иначе False
        return value in self.slots

    def remove(self, value) -> bool:  #
        # возвращает True если value удалено иначе False
        if self.get(value):
            self.slots.remove(value)
            return True
        return False

    def intersection(self, set2):  #
        # пересечение текущего множества и set2
        self.result_powerset = PowerSet()
        for _ in self.slots:
            if set2.get(_):
                self.result_powerset.put(_)
        return self.result_powerset

    def union(self, set2):  #
        # объединение текущего множества и set2
        self.result_powerset = PowerSet()
        self.result_powerset.slots = self.slots.copy()
        for _ in set2.slots:
            self.result_powerset.put(_)
        return self.result_powerset

    def difference(self, set2):  #
        # разница текущего множества и set2
        self.result_powerset = PowerSet()
        for _ in self.slots:
            if set2.get(_) is False:
                self.result_powerset.put(_)
        return self.result_powerset

    def issubset(self, set2):
        # возвращает True, если set2 есть подмножество текущего множества, иначе False
        if self.size() < set2.size():
            return False
        for _ in set2.slots:
            if self.get(_) is False:
                return False
        return True
