# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range(99, 0, -1):
        if (i > 2):
            print(f"{i} bottles of milk on the wall")
            print(f"{i} bottles of milk")
            print("Take one down and pass it around")
            print(f"{i-1} bottles of milk on the wall")
            print()
        elif (i == 2):
            print(f"{i} bottles of milk on the wall")
            print(f"{i} bottles of milk")
            print("Take one down and pass it around")
            print(f"{i-1} bottle of milk on the wall")
            print()
        elif (i == 1):
            print(f"{i} bottle of milk on the wall")
            print(f"{i} bottle of milk")
            print("Take one down and pass it around")
            print("No more bottles of milk on the wall")
            print()
        elif (i == 0):
            print("No more bottles of milk on the wall")
            print("No more bottles of milk")
            print("Go to the store and buy some more")
            print("99 bottles of milk on the wall")
            print()
number_of_bottles()