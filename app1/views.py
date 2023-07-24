from collections import UserList


class CustomList(UserList):
    def __init__(self, iterable):
        super().__init__(self._validate_item(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = self._validate_item(item)

    def insert(self, index, item):
        if index < 0:
            index += len(self.data) + 1

        if index < 0 or index > len(self.data):
            raise IndexError("list index out of range")

        self.data = self.data[:index] + [self._validate_item(item)] + self.data[index:]

    def _validate_and_append(self, item):
        # Custom validation logic for append
        if isinstance(item, (int, float, str)):
            self.data = self.data + [item]

        else:
            raise TypeError(f"Valid data type expected, got {type(item).__name__}")

    def _validate_and_extend(self, other):
        # Custom validation logic for extend
        if isinstance(other, type(self)):
            self.data = self.data + other

        else:
            for item in other:

                if isinstance(item, (int, float, str)):
                    self.data = self.data + [item]

                else:
                    raise TypeError(f"Valid data type expected, got {type(item).__name__}")

    def _validate_item(self, value):
        if isinstance(value, (int, float, str)):
            return value

        raise TypeError(f"Valid data type expected, got {type(value).__name__}")

    def pop(self, index=-1):
        if not self.data:
            raise IndexError("pop from empty list")

        if index < 0:
            index += len(self.data)

        if index < 0 or index >= len(self.data):
            raise IndexError("list index out of range")

        popped_item = self.data[index]
        self.data = self.data[:index] + self.data[index + 1:]

        return popped_item

    def join(self, separator=" "):
        string_joined = ""

        for i, item in enumerate(self.data):
            if i > 0:
                string_joined += separator

            string_joined += str(item)

        return string_joined

    def filter(self, predicate):
        filtered_list = type(self)([])

        for item in self.data:

            if predicate(item):
                filtered_list.append(item)

        return filtered_list

    def for_each(self, func):
        for item in self.data:
            func(item)

    def copy(self):
        return type(self)(self.data)

    def clear(self):
        self.data = []

    def count(self, item):
        return self.data.count(item)

    def remove(self, item):
        self.data = [x for x in self.data if x != item]

    def reverse(self):
        self.data = self.data[::-1]

    def map(self, action):
        return type(self)(action(item) for item in self.data)


my_list = CustomList([1, '2', 3.14, 'hello', 42])
print(my_list)

my_list.append('world')
print(my_list)

my_list.extend([5, '6', 7.77])
print(my_list)

joined_string = my_list.join(", ")
print(joined_string)  # Output: "1, 2, 3.14, hello, 42"

# Using the map method
multiplied_list = my_list.map(lambda x: x * 2)
print(multiplied_list)  # Output: [2, '22', 6.28, 'hellohello', 84]

# Using the filter method
filtered_list = my_list.filter(lambda x: isinstance(x, int))
print(filtered_list)  # Output: [1, 42]

copied_list = my_list.copy()
print(copied_list)  # Output: [1, '2', 3.14, 'hello', 42]

# Using the count method
count_of_2 = my_list.count('2')
print(count_of_2)  # Output: 1

popped_item = my_list.pop()
print(popped_item)
print(my_list)

# Using the remove method
my_list.remove('2')
print(my_list)

# Using the reverse method
my_list.reverse()
print(my_list)

my_list.clear()
print(my_list)

my_list.remove('4')
print(my_list)

