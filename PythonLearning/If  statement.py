is_male = True
is_tall = False

if is_male and is_tall:
    print("Yes, you are a tall male。")
elif is_male and not(is_tall):
    print("you are a short male.")
elif not(is_male) and is_tall:
    print("you are a short male.")
else:
    print("No, you are either not male or not tall or both.")