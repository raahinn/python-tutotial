def say_hi(name):
    print(name + " hi")


def age(user_age):
    print(f'your age is:   {user_age}')


print("top\n")
say_hi("Esahn")
age(25)
print("\n bottom")

print(" Return statement in function")


def cube(num):
    return num * num * num


user_in = int(input("Enter a integer number: "))

print(f'User input is : {user_in}')
print(f'The cube of {user_in} is : {cube(user_in)}')