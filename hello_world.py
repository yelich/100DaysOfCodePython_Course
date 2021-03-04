import math

print("----------------------------")
print("     Even or Odd ")
print("----------------------------")

count = 1

while count > 0:
    num = int(input("Enter a number: "))
    if num == 0:
        print(f"Bye, you're done!")
        break
    elif (num % 2) == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    count += 1