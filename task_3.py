import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        # check i in correct value
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        # check capacity of array
        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        # shift all elements from i to the end of array
        for _ in range(self.count - 1, i - 1, -1):
            self.array[_ + 1] = self.array[_]

        # add itm in i position and raise count
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        # check i in correct value
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        # make new array without i element
        for _ in range(i, self.count - 1):
            self.array[_] = self.array[_ + 1]
        self.array[self.count] = None
        self.count -= 1

        # check capacity of array
        edge = int(self.capacity * 0.5)
        new_capacity = int(self.capacity // 1.5)
        # resize if capacity above 16
        if self.count < edge and new_capacity > 16:
            self.resize(int(self.capacity // 1.5))
            return None
        # resize if capacity 16
        if self.count < edge:
            self.resize(16)
