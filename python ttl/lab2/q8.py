
num = int(input("Enter a number: "))

sum_of_div = 0

for i in range(1, num ):
    if num % i == 0:
        sum_of_div += i

if sum_of_div == num:
    print(f"{num} is a perfect no.")
else:
    print(f"{num} is not a perfect no.")