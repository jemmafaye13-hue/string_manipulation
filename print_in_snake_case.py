name = input("Enter fullname: ")

# 1. Lowercase it
# 2. replace(" ", "_") swaps spaces for underscores
snake = name.lower().replace(" ", "_")
print("Snake Case:", snake)