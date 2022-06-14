class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def __str__(self):
        it = []
        ke = []
        va = []
        for i in range(self.size):
            it.append(i)
            ke.append(self.slots[i])
            va.append(self.values[i])
        return f"{it}->[{ke}]->{va}"

    def hash_fun(self, key: str):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        summa = 0
        for letter in key:
            summa += ord(letter)

        index = summa % self.size
        count = self.size

        while count > 0:
            if self.slots[index] is None:
                return index
            count -= 1
            index = (index + 1) % self.size
        return None

    def is_key(self, key):
        # возвращает True если ключ имеется, иначе False
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        # гарантированно записываем значение value по ключу key
        index = self.hash_fun(key)
        if index is None:
            for _ in range(self.size):
                self.slots.append(None)
                self.values.append(None)
            self.size *= 2
            index = self.hash_fun(key)

        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        # возвращает value для key, или None если ключ не найден
        if self.is_key(key):
            for i in range(self.size):
                if self.slots[i] == key:
                    return self.values[i]
        return None
