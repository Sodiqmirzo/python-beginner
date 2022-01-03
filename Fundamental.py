# temperature = 15
# if temperature > 30:
#     print("It's warm!")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")

# age = 12
# # if age >= 18:
# #     message = "Eligible"
# # else:
# #     message = "Not eligible"
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# and or not
# high_income = False
# good_credit = True
# student = True
# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")
# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")
# if not student:
#     print("Eligible")
# else:
#     print("Not eligible")
# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not eligible")

# # age should be between 18 and 65 (18 <= age < 65)
# age = 22
# # if age >= 18 and age < 65:
# if 18 <= age < 65:
#     print("Eligible")

# for number in range(3):
#     print("Sending email to user", number + 1, (number + 1) * ("."))
# for number in range(1, 4):
#     print("Sending email to user", number, number * ("."))
# for number in range(1, 10, 2):
#     print("Sending email to user", number, number * ("."))

# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# for x in range(5):
#     for y in range(3):
#         print(f"({x},{y})")

# print(type(5))
# print(type(range(5)))
# for x in "Python":
#     print(x)
# for x in [1,2,3,4,5]:
#     print(x)

# number = 100
# while number > 0:
#     print(number)
#     number //= 2
# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers")

# def greet():
#     print("Hi there")
#     print("Welcome aboard")
#
#
# greet()

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")
#
#
# greet("Sodikmirzo", "Sattorov")

# def greet(name):
#     print(f"Hi {name}")
#
#
# def get_greeting(name):
#     return f"Hi {name}"
#
#
# message = get_greeting("Sodikmirzo")
# print(greet("So"))
# print(get_greeting("Sodikmirzo"))

# def increment(number, by):
#     return number + by
#
#
# result = increment(21, 22)
# print(result)

# def increment(number, by=1):
#     return number + by
#
#
# # print(increment(21))
# print(increment(21,22))

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
#
#
# print(multiply(1, 2, 3, 4, 5))

# def save_user(**user):
#     print(user["name"])
#
#
# save_user(id=1, name="Sodikmirzo", age=20)

# message = "a"
#
#
# def greet(name):
#     global message
#     message = "b"
#
#
# greet("Bexruz")
# print(message)

# from pytube import YouTube
#
# yt_url = input("Youtube Url: ")
# yt = YouTube(f"{yt_url}").streams.filter(
#     file_extension="mp4").first().download()
# print(yt)

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
#
#
# print("Start")
# print(multiply(1, 2, 3))

def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    return input


print(fizz_buzz(2))
