is_male = False
is_tall = False

if is_male and is_tall:
    print("male and tall")
elif not(is_male) and is_tall:
    print("not male bot tall")
elif is_male or not is_tall:
    print("not male or not tall")
else:
    print("not male and not tall")