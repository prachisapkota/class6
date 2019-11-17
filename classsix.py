'''PI = 3.14
r = float(input('Enter the radius of the circle :'))
area = PI * r * r
print("Area of the circle is : %.2f" %area)

a=int(input("enter the value"))
b=int(input("enter the power"))
def pow(a,b):
    return a ** b
value=pow(a,b)
print(value)

num=int(input("enter the number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum = sum + (digit**3)
    temp//=10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
print(num)'''

def f_palindrome(n):
    rev_number=0
    while(n)>0:
        num=int(n%10)
        rev_number= rev_number * 10 + num
        n= int(n/10)
    return rev_number
number=int(input("enter the number to check whether it is palindrome"))
pal=f_palindrome(number)
if pal == number:
    print ("it is palindrome")
else:
    print("it is not palindrome")