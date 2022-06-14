class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        summa = 0
        for va in key:
            summa += ord(va)

        return summa % self.size

    def is_key(self, key):
        # возвращает True если ключ имеется, иначе False
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        # гарантированно записываем значение value по ключу key
        pass

    def get(self, key):
        # возвращает value для key, или None если ключ не найден
        if self.is_key(key):
            for i in range(self.size):
                if self.slots[i] == key:
                    return self.values[i]
        return None
