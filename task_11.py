class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.random_digit_1 = 17
        self.random_digit_2 = 223
        self.bitarray = [0b0] * self.filter_len

    def hash1(self, str1):
        # 17
        hash_zero = 0
        for c in str1:
            code = ord(c)
            hash_zero = (hash_zero * self.random_digit_1 + code) % self.filter_len
        return hash_zero

    def hash2(self, str1):
        # 223
        hash_zero = 0
        for c in str1:
            code = ord(c)
            hash_zero = (hash_zero * self.random_digit_2 + code) % self.filter_len
        return hash_zero

    def add(self, str1):
        # добавляем строку str1 в фильтр
        self.bitarray[self.hash1(str1)] = 0b1
        self.bitarray[self.hash2(str1)] = 0b1

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        if self.bitarray[self.hash1(str1)] == 0b1 and \
                self.bitarray[self.hash2(str1)] == 0b1:
            return True
        return False
