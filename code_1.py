#Convret usd in Inr

USD = int(input("Enter you USD value : "))

def conv_USD(USD): #we defined a Funtion

    INR = 96 * USD

    print(USD, "USD =", INR, "INR")

    return INR

#calling the Funtion for Conversion

conv_USD(USD)

#Something new
 
print("Shradha Didi", end= " ") #Getting the output in the same line

print("Apna_college") #the second out


#Making a new tupple in  Function

cities =("Mumbai", "Delhi", "Kolkata", "Chennai", "Bombay")

Actor = ("SRK", "SALMAN", "RAJ SHAMANI")

def val_city(city):

    print(len(city))

    print(Actor, end= " " )

    print("ALL ARE GOOD ACTORS")

    return city

val_city(cities)


def facto_of_num(n):

    fact = 1

    for i in range(1, n + 1):

        fact = fact * i

    print(fact)

    return fact

facto_of_num(6)

#store items prices

laptop_price = int(input("Enter your laptop price : "))

mouse_price = int(input("Enter your mouse price : "))

keyboard_price = int(input("Enter your keyboard price : "))

#defining a function to calculate toatl price

def total_price(laptop, mouse, keyboard):

#incliding GST with total price

    total = (laptop + mouse + keyboard)*0.18 + (laptop + mouse + keyboard)

    print("total price :", total)

    return total

total_price(laptop_price, mouse_price, keyboard_price)

#Homework



#recursion
def display_num(num):
    if num == 1:

        return 

    print(num)

    display_num(num - 1)

display_num(4)

def calculate_storage(folder_depth, size_per_folder):

    if folder_depth == 0:

        print("Root reached. Storage scan complete.")

        return
    
    print(f"folder_level", folder_depth, size_per_folder)

    calculate_storage(folder_depth - 1, size_per_folder)


calculate_storage(4, 250)
print("Total Storage Used :", 4 * 250 , "MB")

#calculatinn dfactortial
def facto(n):

    if (n == 0 or n == 1):

        return 1
    
    return facto(n-1) * n

n = int(input("Enter your num : "))
print(facto(n))

#defining a Function
def facor(n):

# conditional statement:

    if (n == 0 or n == 1):

        return 1

    return facor(n-1) * n #statement output

#defining statement in variable

num = int(input("Enter your value"))

#calling the existing function

factorial = facor(num) #storing  in variable

#printing the output: 

print(f"factorial of {num} is :", factorial)
