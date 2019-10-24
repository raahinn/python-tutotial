# power of any number

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

a = int(input("Inter the base Number: "))
b = int(input("Inter the power Number: "))
print(raise_to_power(a, b))
print("work done")