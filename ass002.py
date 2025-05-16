
a=int(input("Enter a number: "))

if a % 2 == 0:
    print(a,"Is an even number.")
else:
    print(a,"Is an Odd number")


total=0
for number in range(1,51):
    total += number
print("The sum of numbers from 1 to 50 is: ",total)