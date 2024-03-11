class SortedDict:
    def __init__(self):
        # these lists are private because we don't wan't users to mess with them!
        self.__keys = []
        self.__values = []

    def add(self, k, v):
        if self.__keys == []:
            self.__keys.append(k)
            self.__values.append(v)
        elif k in self.__keys:
            index = self.__keys.index(k)
            self.__keys[index] = k
            self.__values[index] = v
        else:
            for index, key in enumerate(self.__keys):
                if k < key:
                    self.__keys.insert(index, k)
                    self.__values.insert(index, v)
                    return
            self.__keys.append(k)
            self.__values.append(v)

    def items(self):
        res = []
        for index, k in enumerate(self.__keys):
            res.append((k, self.__values[index]))
        return res

    def remove(self, k):
        try:
            index = self.__keys.index(k)
        except ValueError:
            raise IndexError(f"key {k} not in SortedDict!!")
        del self.__keys[index]
        del self.__values[index]

    def __add__(self, other): # +
        temp = SortedDict()
        for k, v in self.items():
            temp.add(k,v)
        for k, v in other.items():
            temp.add(k,v)
        return temp

    def __sub__(self, other): # -
        temp = SortedDict()
        filter_keys = []
        for k, v in other.items():
            filter_keys.append(k)
        for k, v in self.items():
            if k not in filter_keys:
                temp.add(k, v)
        return temp

    def __str__(self):
        res = ""
        for index, k in enumerate(self.__keys):
            res += f"{k}: {self.__values[index]}\n"
        return res

s1 = SortedDict()
s1.add(1, "foo")
s1.add(3, "bar")
s1.add(2, "baz")
print(s1)

s2 = SortedDict()
s2.add(3, "bazzzz")
s2.add(0, "hallo")
print(s2)

print(s1 + s2)
print(s1 - s2)
