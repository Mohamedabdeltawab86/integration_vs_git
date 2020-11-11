# a = 3
# b = 3
# c = 4
# d = 4
# if a == b:
#     if c == d:
#         match = True 

# student = [
#     {
#         "d": "dinner"
#     }
# ]
# print(student)
"""------------------------------------------------------
# dict = {
#   "list_0": [3, 1, 6],
#   "list_1": ["apples", "pears", "oranges"],
#   "list_2": [True, False, True],
# }
# index_number = 0
# for element in dict["list_2"]:
#   if element == False:
#     print(index_number)
#   else:
#     index_number += 1
---------------------------------------------------------"""


"""------------------------------------------------------
customers = {
  0: {
    "first name":"John",
    "last name": "Ogden",
    "address": "301 Arbor Rd.",
  },
  1: {
    "first name":"Ann",
    "last name": "Sattermyer",
    "address": "PO Box 1145",
  },
  2: {
    "first name":"Jill",
    "last name": "Somers",
    "address": "3 Main St.",
  },
}
print(customers[1]["last name"])

friends = ["Ross", "Rachel", "Monica", "Phoebe", "Gunther", "Joey", "Chandler"]
not_really_a_friend = friends.pop(4)
print(not_really_a_friend)

class Product():
    def __init__(self, color):
        self.color = color
    def __repr__(self):
        return "<__main__.Product: color = " + str(self.color) + ">"

chair = Product("red")
print(chair)
print(Product)

class Performer():
  def __init__(self, act, gender):
    self.act = act
    self.gender = gender
print(Performer)
ivana = Performer("trapeze", "female")
alexi = Performer("clown", "male")
print(ivana)
print(alexi)

---------------------------------------------------------"""


class Student():
  def __init__(self, age, gender, major):
    self.age = age
    self.gender = gender
    self.major = major
id90 = Student(20,"f", "computer science")
print(id90.gender)
