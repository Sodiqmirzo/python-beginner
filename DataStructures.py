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

