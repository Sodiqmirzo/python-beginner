# letters = ['a', 'b', 'c', 'd']
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 5
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("Hello World")
# print(len(chars))

# letters = ['a', 'b', 'c', 'd', 'e', 'j']
# numbers = list(range(20))
# letters[0] = "A"
# print(letters[0])
# print(letters[0:3])
# print(letters[:3])
# print(letters)
# print(letters[::2])
# print(letters[::-1])
# print(numbers[3::2])
# print(numbers[::-1])

# numbers = [1, 2, 3, 4, 5, 6, 6, 6, 68]
# # first, second, *other = numbers
# first, *other, last = numbers
# print(first, last)
# print(other)

# letters = ['a', 'b', 'c', 'd', 'e', 'j']
# for index, letter in enumerate(letters):
#     print(index, letter)

# letters = ['a', 'b', 'c', 'd', 'e', 'b', 'j']
#
# # Add
# letters.append("some")
# letters.insert(0, '-')
# print(letters)
#
# # Remove
# letters.pop()
# letters.pop(0)
# letters.remove("b")
# print(letters)
# del letters[0:3]
# letters.clear()
# print(letters)

# letters = ['a', 'b', 'c', 'd', 'e', 'b', 'j']
# print(letters.count("some"))
# if "some" in letters:
#     print(letters.index("some"))
# print(letters.index("a"))

# numbers = [3, 23, 21, 45, 65, 77, 54, 27, 2]
# # numbers.sort()
# # numbers.sort(reverse=True)
# # print(sorted(numbers))
# # print(sorted(numbers, reverse=True))
# # print(numbers)
# item = [("Product1", 10), ("Product2", 32), ("Product3", 4)]
#
# # def sort_item(item):
# #     return item[1]
#
#
# # item.sort(key=sort_item)
# # item.sort(key=lambda parameteres: expression) structure lambda fun
# item.sort(key=lambda item: item[1])
# print(item)

# items = [("Product1", 10), ("Product2", 32), ("Product3", 4)]
# prices = list(map(lambda item: item[1], items))
# print(prices)

# items = [("Product1", 10), ("Product2", 32), ("Product3", 4)]
# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)

# items = [("Product1", 10), ("Product2", 32), ("Product3", 4)]
# # prices = list(map(lambda item: item[1], items))
# prices = [item[1] for item in items]
# print(prices)
# # filtered = list(filter(lambda item: item[1] >= 10, items))
# filtered = [item for item in items if item[1] >= 10]
# print(filtered)

# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30]
# # [(1, 10), (2, 20), (3, 30)]
# print(list(zip("abs", list1, list2)))

# browsing_session = []
# browsing_session.append(1)
# # browsing_session.append(2)
# # browsing_session.append(3)
# # print(browsing_session)
# # last = browsing_session.pop()
# # print(last)
# # print(browsing_session)
# # print("redirect", browsing_session[-1])
# # if not browsing_session:
# #     print("disable")
# browsing_session.pop()
# if not browsing_session:
#     browsing_session[-1]

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print("empty")

point = (1, 2, 4)
# point = (1, 2) + (3, 4)
# point = (1, 2) * 3
# point = tuple([1, 2])
# point = tuple("Hello World")
# print(type(point))
# print(point)
# print(point[0:2])
# if 10 in point:
#     print("exist")
#
# point[0] = 10

# x = 10
# y = 11
# # z = x
# # x = y
# # y = z
# x, y = y, x
# print(f"x: {x} \ny: {y}")

# from array import array
#
# numbers = array("i", [1, 2, 3])
# numbers[0] = 1.0
# print(numbers)
# # https://www.educative.io/edpresso/what-are-type-codes-in-python

# numbers = [1, 1, 2, 3, 4]
# # uniques = set(numbers)
# first = set(numbers)
# # print(uniques)
# second = {1, 5}
# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)
#
# if 1 in first:
#     print("Yes")

# point = {"x": 1, "y": 3}
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20
# # print(point)
# if "a" in point:
#     print(point["a"])
# print(point.get("a", 0))
# del point["x"]
# print(point)
# # for x in point:
# #     print(x)
# # for key in point:
# #     print(key, point[key])
# # for x in point.items():
# #     print(x)
# for key, value in point.items():
#     print(key, value)

# # values = []
# # for x in range(5):
# #     values.append(x * 2)
# # print(values)
# # [expression for item in items]
# # values = [x * 2 for x in range(5)]
# # values = {x * 2 for x in range(5)}
# # values = {}
# # for x in range(5):
# #     values[x] = x * 2
# values = {x: x * 2 for x in range(5)}
# print(values)

# from sys import getsizeof
#
# # values = [x * 2 for x in range(10)]
# values = (x * 2 for x in range(1000))
# print("gen:", getsizeof(values))
# values = [x * 2 for x in range(10)]
# print("list:", getsizeof(values))
# # for x in values:
# #     print(x)

# # numbers = [1, 2, 3, 4, 5]
# # # print(numbers)
# # print(*numbers)
# # values = list(range(5))
# # values = [*range(5), *"Hello"]
# # first = [1, 2]
# # second = [3]
# # values = [*first, 'a', *second, *"Hello"]
# # print(values)
# first = {"x": 1}
# second = {"x": 10, "y": 2}
# compined = {**first, **second, "z": 89}
# print(compined)

# from pprint import pprint
#
# sentence = "This is a common interview question"
#
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# # pprint(char_frequency, width=1)
#
# char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)
# print(char_frequency_sorted[0])
