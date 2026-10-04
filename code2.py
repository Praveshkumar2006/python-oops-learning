# def calculate_price(items_count,items_price, GST_value):

#     if (items_count == 0):

#         print("ROOT reached")

#         return 0
    
#     print(f"Count: {items_count}, Price: {items_price}, GST: {GST_value}")

#     absolute_total = items_price + (items_price * GST_value)

#     return absolute_total  + calculate_price(items_count - 1, items_price, GST_value)


# #calling the funtion

# m = int(input("Enter count:"))

# n = float(input("Enter price :"))

# o = float(input("Enter GST rate :"))


# total = calculate_price(m, n, o)

# print(f" total Price = {total}")

# #Find factorial

# def fact(n):

#     if (n == 0 or n == 1): #applying the base case

#         return 1
    
#     return fact(n - 1) * n #returning output

# #defining the function

# num = int(input("Enter your num : ")) #taking the input from the user

# factorial = fact(num) #defining operation in variable

# print(f"factorial of {num} is ", factorial)


# #Oject orientation rogramming ayatem

# class Student: #creating class

#     name = "Tony stark" #blueprint


# s1 = Student() #creating object

# print(s1.name)

# s2 = Student

# print(s2.name)

# class avengers:

#     avenger1 = "Tony stark"

#     avenger2 = "Captain America"

#     avenger3 = "Hulk"

# Avengers = avengers()

# print(Avengers.avenger1)

# print(Avengers.avenger2)

# print(Avengers.avenger3)

# #constructor

# class Student: #defining the class name

#     name = "Tony stark"

#     #MAKING THE CONSTRUCTOR>>>>>>>>>

#     def __init__(self, Name, Age, Home): #defining the function

#         self.Name = Name

#         self.Age = Age

#         self.Home = Home

#         print("Adding new student in Database")

# s1 = Student("Tony stark", 45, "America") #Student 1 Data

# print(s1.Name, s1.Age, s1.Home)

# s2 =  Student("Captain America", 40, "California") #Student 2 Data

# print(s2.name, s2.Age, s2.Home)

# class Student:

#     #class attribute

#     college_name =  "ABC college"

#     name = "Anonymous"

#     def __init__(self, name, Age):

#         #object attributes

#         self.name = name

#         self.Age = Age

#     def welcome(self):

#         print("Welcome Student", self.name)

# s1 = Student("tony", 34)

# s1.welcome()

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0

#         for val in self.marks:
#             sum += val

#         print("Hi", self. name, " Your avg score is : ", sum/3)

# s1= Student("Tony", [97, 98, 99])

# s1.name = "Iron man"

# s1.get_avg()

# # #Static Method
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.acc = True
#         self.cluth  = True
#         print("car started")
# car1 = Car()
# car1.start()

# class PNB: 
#     #defing the self
#     def __init__(self, account, balance): #object attribute

#         self.account = account
#         self.balance = balance
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("Total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("Total balance =", self.get_balance())
#     def get_balance(self):
#         return self.get_balance


# payment1 = PNB("JPR", 1000000)
# payment1.debit(500)
# payment1.credit(50000)
# print(payment1.account, payment1.balance)
# class RBI:
#     def __init__(self, name, Account, balance):

#         self.name = name
#         self.Account = Account
#         self.balance = balance

#     def debit(self, amount):

#         self.balance -= amount
#         print(f"Rs.", amount, "Cr. was debited")
#         print("Total balance =", self.get_balance())

#     def credit(self, amount):

#         self.balance += amount
#         print(f"Rs.", amount, "Cr. was credited")
#         print("Total balance", self.get_balance())

#     def get_balance(self):
#         return self.balance

# payment = RBI("Tony stark", 337200, 522)

# payment.debit(56)

# payment.credit(500)

# print(payment.name)
# print(payment.Account)
# print(payment.balance, "= Cr.")




class Lightbulb:

    def __init__(self, room_name):
        self.room_name = room_name
        self.is_on = False 
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
        print(f"the light in {self.room_name} is now OFF!")

my_bulb = Lightbulb("bedroom")
my_bulb.turn_on()
my_bulb.turn_off()