name = input("Enter fullname: ")

# 1. Title case it
# 2. replace(" ", "") removes all spaces
pascal = name.title().replace(" ", "")
print("Pascal Case:", pascal)