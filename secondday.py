

num=123
total=0
for i in str(num):
 total=total+int(i)
print(total)

'''
if round(0.1 + 0.2,2) == 0.3:
 print("Equal")
else:
 print("Not Equal")

gender=str(input('Enter a gender:'))
if gender =='M':
 print('Male') 
elif gender=='F':
 print("Female") 
elif gender=='O':
 print("Others")  
else:
 print("Invalid gender") 


 i=0
while i<3:
 print(i)
 i=i+1

print(2 in range(0,5,1))

for x in range(0,5,2):
 print(x)
 

for i in range(0,5,1): 
 print('Swara')
 i=i+1

range(5) 


#Palindrome check
text=input("enter a text:")
check=text.replace(" ", "").lower()
reverse=check[::-1]
print("Given string: "+check)
print("Reverse string: "+reverse)

if check==reverse:
 print("Palindrome")
else:
 print("Not palindrome")


 # ASCII sum
 def sum_of_ascii(text):
    total = 0
    for char in text:
        total += ord(char)  # ord() gives ASCII value of character
    return total

user_Input=input("enter a text:")
result=sum_of_ascii(user_Input)
print("Sum of ASCII values: " , result)

user_Input=input("enter a text:")
print(sum(ord(ch) for ch in  user_Input))
 '''