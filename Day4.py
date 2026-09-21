def is_prime_number():
    number = 17
    is_prime = True

    if number <= 1:
        is_prime = False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

is_prime_number()

"""
def add_sum(a,b):
    return a+b
result=add_sum(10,2)
print(result)

a=10
b=12
def get_sum():
    b=18
    return a+b
result=get_sum()
print(result+b)
    

a=10
def sum():
    #print(a)
    a=89
    b=12
    return a+b
print(sum())



score=int(input("enter your score:"))
if score >= 90:
    print("Grade: A")
    print("Excellent work!")
elif score >= 80 and score< 90:
    print("Grade: B")
    print("Good job!")
elif score >= 70 and score< 80:
    print("Grade: c")
    print("Satisfactory")
elif score >= 60 and score< 70:
    print("Grade: D")
    print("Needs improvement")
elif score < 60 and score >=50:
    print("Grade: F")
    print("Failed")
elif score == 100:
    print("Perfect score!")
elif score < 50:
    print("Please see instructor")


 age = 15
is_student = True

if age < 18:
    if is_student:
        price = 5
    else:
        price = 7
else:
    if is_student:
        price = 8
    else:
        price = 10

# Output result
print("Ticket price: $" + str(price))   


username = "admin"
password = "secret123"


if not username:
    print("Error: Username is required.")
elif not password:
    print("Error: Password is required.")
elif username != "admin":
    print("Error: Username is incorrect.")
elif password != "secret123":
    print("Error: Password is incorrect.")
else:
    print("Login successful!")



number=456
print("Ones= ",number % 10)
print("Tens= ",(number // 10) % 10)
print("Hundreds= ",number // 100)



hours = 2
minutes = 30
seconds = 45
total_seconds = (hours * 3600) + (minutes * 60) + seconds
print(f"Total seconds: {total_seconds}")



bill_amount = 85.00
tip_rate = 0.18
people = 4


tip_amount = bill_amount * tip_rate
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / people


print("Bill amount: $", bill_amount)
print("Tip (18%): $",round(tip_amount,2))
print("Total amount: $",total_amount)
print("Amount per person (4 people): $",round(amount_per_person,2))


names = ["Alice", "Bob", "Emily", "David", "Oliver", "Sarah"]
vowels = ("A", "E", "I", "O", "U")
count = 0
for name in names:
    if name.startswith(vowels):
        count += 1
print(f"Number of names starting with a vowel: {count}")


numbers = [45, 23, 67, 89, 12, 56]
max_value = max(numbers)
max_index = numbers.index(max_value)
print(f"Maximum value: {max_value}")
print(f"Position: {max_index}")



numbers = [5, 2, 8, 2, 9, 2, 1, 2]
target = 2
indices = []
for index, value in enumerate(numbers):
    if value == target:
        indices.append(index)
print("Value ",target,"found at positions: ",indices)


def countdown():
    for i in range(10, 0, -1):
     print(i, end=" ")
     
countdown()
print()
print("Go!")


def celsius_to_fahrenheit():
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")

celsius_to_fahrenheit()
"""