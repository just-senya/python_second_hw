class CustomList:
    def __init__(self, number_list = list()):
        self.numbers = number_list[:]
        self.length = len(number_list)

    def __repr__(self):
        return repr(self.numbers)

    def __size(self):
        size = int(0)
        for value in self.numbers:
            size += value
        return size
    
    def __add__(self, add):
        result = list()

        if isinstance(add, CustomList) is True:
            result = add.numbers[:]
        elif isinstance(add, list) is True:
            result = add[:]
        else:
            raise TypeError
        
        result_len = len(result)
        
        if result_len < self.length:
            result += [0] * (self.length - result_len)

        for index in range(self.length):
            result[index] += self.numbers[index]

        return CustomList(result)

    def __sub__(self, subtrac):
        result = list()

        if isinstance(subtrac, CustomList) is True:
            result = [-value for value in subtrac.numbers]
        elif isinstance(subtrac, list) is True:
            result = [-value for value in subtrac]
        else:
            raise TypeError
        
        result_len = len(result)
        
        if result_len < self.length:
            result += [0] * (self.length - result_len)

        for index in range(self.length):
            result[index] += self.numbers[index]

        return CustomList(result)

    def __lt__(self, compare):
        if self.__size() < compare.__size():
            return True
        return False
    
    def __gt__(self, compare):
        if self.__size() > compare.__size():
            return True
        return False

    def __le__(self, compare):
        if self.__size() <= compare.__size():
            return True
        return False

    def __ge__(self, compare):
        if self.__size() >= compare.__size():
            return True
        return False

    def __ne__(self, compare):
        if self.__size() != compare.__size():
            return True
        return False

    def __eq__(self, compare):
        if self.__size() == compare.__size():
            return True
        return False

A = CustomList([3, 3, 3, 5])
B = CustomList([1, 2, 3, 4])
#print(A - B)
