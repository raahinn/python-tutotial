# list is like array
'''
friends = ["ismil", "karen", "siam"]

print(friends[1])
print(friends[0:2])
print(friends[0:1])
print(friends)

'''

print("**** list functions")
lucky_number =[4, 5 , 56, 6, 65]
friends = ["ismil", "karen", "siam"]
friends.extend(lucky_number)
print(friends)

lucky_number.append("ced")
print(lucky_number)

lucky_number.insert(1, "kelly")
print(lucky_number)

lucky_number.insert(2, 9999)
print(lucky_number)

lucky_number.remove("kelly")
print(lucky_number)

lucky_number.pop()
print(lucky_number)

print(lucky_number.index(6))

lucky_number.sort()
print(lucky_number)

