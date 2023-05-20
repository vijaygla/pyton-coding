# TO CHECK ASKII VALUE OF ANY ENGLISH ALPHABETS WE USE ord OR chr.
a="A"
b="Z"
c=ord(a)
d=ord(b)
print(f"askii value is {c}\naskii value of  is {d}")



# Program to print current Day,date and time.
import time
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
print(str);



# EXERCISE - 1               Total no. of question = 20

# 1.program to print two differnt string "hello" and "world" in different.
print('"hello"\n"world"')


# 2.program to print two different string "hello" and "world" in single line.
print('"hello" "world"')


# 3.program to add two input value.
a=int(input('enter the value of a:'))
b=int(input('enter the value of b:'))
print(f'sum of a and b is = {a+b}')


# 4.program to subtract to integer intered value.
a=int(input("enter the value of a in integer:"))
b=int (input ("enter the value of b in integer :"))
print(f'sum of two integer inter value is = {a+b}')


# 5.program to munltiply two entered integer value.
a=int (input ("enter the value of a:"))
b=int (input ("enter the value of b in integer:"))
print(f"product of a and b is = {a*b}") 


# 6.program to input two integer value and calculate first number raised to the power second number.
a=int (input ("enter the value of a:"))
b=int (input ("enter the value of b:"))
print(f"first number raised by power of second  {a**b}")


# 7.program to find area and perimeter of rectangle,when required to input thhe length and breath entered by user.
l=float (input ("length of rectangle:"))
b=float (input ("breath of rectangle:"))
print(f"perimeter of rectangle is = {2*(l+b)}\narea of rectangle is = {l*b}")


# 8.program to find the area and circumference of a circle,when the radius is enterd by the user.
r=float(input ("eneter the value of radius"))
print(f"circumference of circle is = {2*3.14*r}\nArea of circle is = {3.14*r**2}")


# 9.program to find the hypotenuse of a right angled triangle ,when base and height are entered by the user.
#let us cosider the base=b  &  height=h   H=hypotenuse
h=float (input ("enter height of right angled triangle:"))
b=float (input ("enter the base of ||:"))
print(f"Hypotenuse of right angled trianle abc is = {h**2+b**2}")



# 10.program to input two number and print the swapped value of them.
a=int (input ("enter the value of a: "))
b=int (input ("enter the value of b: "))
print(f"befor swapped a = {a} and b = {b}\nafter swapped a = {b} and b = {a}")




# 11.program to find the number of currency notes of each types (Rs. 2000, Rs.500 and Rs. 100),
# when  the total number of currency notes counted altogether is minimum and there must be at
# least a 100 rupee notes dispensed.The amount to be withdraw is to be entered by the user.
a=int(input("enter the amount of money for withdrwal:")) #a=amount
a=a-100
print(f"no. of 2000 notes is = {int (a/2000)}")
a=a%2000
print(f"no. of 500 notes is = {int (a/500)}")
a=a%500
print(f"no. of 100 rupees notes is = {int (1+(a/100))}")



# 12.program to find wheather the triangle is scalene,isosceles and right angled triangle or invalid when the sides of the triangle is entered by the user.
a=int (input ("enter the 1st side of triangle:"))
b=int (input ("enter the 2nd side of triangle:"))
c=int (input("enter the 3rd side of the triangle:"))
if a==b==c:
    print("triangle is eqilateral")
elif a==b or b==c or c==a:
    print("isoscelse triangle")
elif a**2==b**2+b**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
    print("Right angeled triangle")
else:
    print("scalene triangle")



# 13.program to find the to find the simple interest and the total amount when the principal,rate of Interest and Time are entered by the user.
p=int (input ("enter the principal:"))
r=int (input("enter the value of rate:"))
t=int (input ("enter the time in month:"))
print(f"SIMPLE INTEREST IS = {(p*r*t)/100}")
i=int ((p*r*t)/100)
print(f"TOTAL AMOUNT IS = {p+i}")



# 14.program to find the compound intrest compounded annually and the total amount when the principal,rate of intrest and time are enterd by the user.
# (Total amoungt) A = P (1 + r/n)^nt
# (comound intrest) C=p(1+r/n)^nt - p
p=float (input ("enter the principal:"))
r=float (input ("enter the rate:"))
t=float (input ("enter the time:"))
n=float (input ("number of compound frequency:"))
a=(1+r/n)
c=(p*a**n*t)-p
b=p+c
print(f"Compound intrest is = {c}\nTotal amount is = {b}")



# 15.program to calculate the number of rectangular tiles required to cover a  rectangular floor if
# the dimension of the floor and the dimension of tiles are entered by the user.
a=int (input ("enter the length of floor:"))
b=int (input ("enter the breath of floor:"))
c=int (input ("enter the length of tile:"))
d=int (input ("enter the breath of tile:"))
A=a*b
a=c*d
print(f"No. of tile required to cover is = {int (A/a)}")



# 16.program to input the number of overs in the cricket match and output the maximum runs a 
# player can score in the match.Assume that there are no extra runs or NO balls in the match
# played for example, in a 50 over match,the miximum runs scored are 1653.
over=int (input ("enter the no. of over:"))
max=(over-1)*33
Max=36+max
print(f"Maximum run can scored in {over} over is = {Max}")

# input:
# over=2
# output:
# Maximum run can scored in 2 over is = 69



# 17.program to input the number of heads and legs in a farm and identify the number of hen 
# and goats in the farm.for example,if there are 340 heads and 1060 legs there are 150 hen and 190 goats.
head=int (input ("enter the no. of head:"))
leg=int (input ("enter the no. of leg:"))
goat=(leg-2*head)/2
hen=head-goat
print(f"Total number of Goat is = {goat}\nTotal number of Hen is = {hen}")






# 18.program to find wheather the input number is even or odd.
a=int (input("enter any integer number:"))
if (a%2)==0:
    print("even")
else:
    print("odd")


# 19.program to input two number and subtract the smaller number from the greatest number.
a=int (input ("enter any number:"))
b=int (input ("enter any number:"))
if a>b:
    print(f"Difference is = {(a-b)}")
else:
    print(f"Difference is = {(b-a)}")



# 20.A man has certain number of apples.
# if he picks them in a group of 7, he can pick all of them.
# if he picks them in a group of 6,1 apple is left behind.
# if he picks them in a group of 5,1 apple is left behind.
# if he picks them in a group of 4,1 apple is left behind.
A=7  #total no. of apple 
b=int (input ("enter no. of apple in left hand:"))
c=int (input ("enter no. of apple in right hand:"))
if (b+c)==7:
    print("NO any apple left")
elif (b+c)>7:
    print("invalid enter")
else:
    print(f"No.of apple left is = {A-(b+c)}")

# EXERCISE - 1  COMPLETED.

# Class work
# tuesday     14-02-2023

# 1.program to print no of day in  all the month.
m=int (input("enter the value of month like for january press 1 : "))# m=month
d=(m<=7)*(30+(m%2))+(m>7)*(31-(m%2)) - (m==2)*2          # d=day
print(d)


# 2.program take the age of man and name and print that the eligible for vote or note by using the logical operator.
a=int(input ("enter your age:"))
b=str(input ("enter your name:"))
(a>=18) and print( f"{b} is eligible for vote")
(a<18) and print(f"SORRY {b} you are not eligible for vote")


# ALTERNATE METHOD
a=int(input ("enter your age:"))
b=str(input ("enter your name:"))
(a<18) or print(f"{b} you are eligible for vote")
(a>=18) or print(f"{b} you are not eligible for vote ")


# 3.program to print check wheather the input string are sustring of other string or not.
a=input(("enter the string:"))
b=input(("enter the other string:"))
print(b in a)
print(b not in a)



# 4.example of xor and other operator.
a=68
b=22
c=a^b
print(c)




# 5.program to find the hamming distance of two number.
# hamming distance:-Distance between two number in bits.
a=int(input('enter the 1st number:'))
b=int (input("enter the 2nd number:"))
c=0
e=a^b



# 6.program to check the year is leap or not.
year=int (input("enter the year:"))
if (year%4==0 and year%100!=0):
    print(f"{year} is a leap year")
elif (year%400==0):
    print(f"{year} is a leap year")
else:
     print(f"{year} is not a leap year")




# 7.program to check the greatest number out of three input number by user.
c=int (input ("enter the value of c:"))
a=int (input ("enter the value of a:"))
b=int (input ("enter the value of b:"))
if (a>=b) and (a>=c):
    print(f"{a} is greatest")
elif(b>=a) and (b>=c):
    print(f"{b} is greatest")
elif(c>=a) and (c>=b):
    print(f"{c} is greatest")
else:
    print("Good you are unique")



# EXAMPLE OF SHORT HAND IF ELSE (TERNARY)
a=int(input("enter the value of a:"))
print("even") if a%2==0 else print ("odd")


# 8.program to print the given number is positive negative or zero.
a=int (input("enter the number:"))
if(a>0):
    print("positive")
elif(a<0):
    print("negative")
else:
    print('Zero')



# note:-by default the value of sep keyword argument 
# EXAMPLE
a=10
b=3
print(a/b)
print(a//b)
print(a,'divide',b,'=',a//b,sep='*')

# to not change the line in python by default we use 
a=10
b=3
print(a,end=' ')
print(b,end=' ')
print(a,end='*')
# note:-by default the value of end keyword argument is in new line character but we can change it by assinging a new value(string) to it.
# note:-by default python give float value up to 16 digit after the decimal.

# using of dot format in printing the python programming.
a=10
b=3
print('{0} divide {1} is {2}'.format (a,b,a/b))
print('a={0}'.format(a))
# limitation
# 1.index remembering

# using of formated string 
# using of float decimal value op to what time need
a=10
b=3
print(f"{a} divide {b} is = %.{a/b} \n and also {a//b}")
print("%d divide %d is %.f(a,b,22/7)")
print("%d divide %d is %.3f(a,b,a/b)")




# 1.program to check the greatest(maximum) of three number given by the user.
a=int(input("enter the value of a:"))
b=int (input ("enter the value of b:"))
c=int(input ("enter the value of c:"))
d=(a>b) and (b>c)
print(f"greatest number is = {a}")
e=(b>a) and (b>c)
print(f"Greatest number is = {b}")
f=(c>a) and (c>b)
print(f"Greatest number is = {c}")



# # 2.program to check the types of triangle or to check the invalid 
# # condition ---sum of two side must be greater than the 3rd side so triangle will valid
a=int (input("enter the side of triangle:"))
b=int (input("enter the side of triangle:"))
c=int (input("enter the side of triangle:"))
if((a+b)>c and (b+c)>a and (c+a)>b):
    print("Valid triangle")
else:
    print("Invalid triangle")
if(a==b==c):
    print("equilateral triangle")
elif((a==b and b!=c) or (b==c and c!=a) or (c==a and c!=b)):
    print("isosceles triangle")
elif (a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2):
    print("right angled triangle")
else:
    print("scalene triangle")



# 3.program to take the coordinate of point from user and print the quadrant,asis, or origin.
a=int (input("enter the coordinate of x axis:"))
b=int (input ("enter theh coordinate of y axis:"))
if (a==0 and b==0):
    print(f"point is at origin\nno quadrant\nno  axix ")
elif (a==0 and b!=0):
    print(f"not at origin\nat x axis\n1st quadrant")
elif(a>0 and b>0):
    print(f"1st quadrant\n not on x and y axis")
elif(a<0 and b<0):
    print(f"3rd quadrant ")
elif(a<0 and b>0):
    print(f"2nd quadrant")
elif (a>0 and b<0):
    print(f"4th quadrant")
else:
    print(f"enter is invalid!")



# 4.program to check wheather the given number is divisible by the 7 or 3 or not.
a=int(input("enter the number:"))
if(a%7==0 or a%3==0):
    print(f"enter number is divisble")
else:
    print("enter the number is not divisible")



# 5.program to take the coordinate of centre of circle and area of circle and coordiante of
# an arbitary point from the user and check wheather it lies inside  circle outside circle or at boundary. 
a=int (input("enter the x coordinate of center of circle:"))
b=int (input("enter the y coordinate of center of circle:"))
c=int (input("enter the x coordinate on the  circle:"))
d=int (input("enter the y coordinate on the  circle:"))
area=int (input("enter the area of circle:"))
r=(area/3.4)**(1/2)
d=((a-c)**2 + (b-d)**2)**(1/2)
if(d==0):
    print(f"point at the center")
elif(d>r):
    print(f"point outside the circle")
elif(d<r):
    print(f"point inside the circle")
else:
    print(f"ivalid")








# PYTHON PROGRAM TO MAKE A MINI CALCULATOR ?
a=int(input("enter the first number : "))
op = input("enter the operator you want to use {+,-,*,/,%,**} : ")
b=int(input("enter the second number : "))
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op=="/":
    print(a/b)
elif op=="%":
    print(a%b)
elif op=="**":
    print(a**b)
else:
    print("Thanku not possible operator!")





# 1. Program to find the maximum of the three entered numbers.
a=int(input("enter the no.:"))
b=int(input("enter the no.:"))
c=int(input("enter the no.:"))
if((a>b) and (b>c)):
    print(f"{a} is the maximum of three  number")
elif((b>a) and (b>c)):
    print(f"{b} is the maximum of tyree number")
else:
    print(f"{c} is the maximum of three number")



# 2.Program to input the centre of a circle, radius of the circle and an arbitrary point P(x,y) and 
# determine whether the point is inside the circle, on the circle or outside the circle.
a=int(input("enter the coordinate of center of x axis:"))
b=int(input("enter the coordinate of center of y axis:"))
c=int(input("enter the coordinate of point  of x axis:"))
d=int(input("enter the coordinate of point  of y axis:"))
area=float(input("enter the area of of circle:"))
r=(area/3.14)**(1/2)
d=((c-a)**2+(d-a)**2)**(1/2)
print("OUTPUT:-")
if(d<r):
    print("point is inside the circle")
elif(d>r):
    print("point is outside the circle")
elif(d==0):
    print("point is origin itself")
else:
    print("not valid input")



# 3.Big Bazaar specifies its customers into three categories as Bronze, Silver and Gold. If the 
# shopping amount is greater than 25000, the category is GOLD. If the shopping amount is 
# between 10000 and 25000, the category is SILVER, otherwise the category is BRONZE. The 
# discount offered for GOLD customers is 20% of the shopping amount, for SILVER customers is 
# 10% of the shopping amount and 5% otherwise. Design a program in python that asks the user 
# to input the total shopping amount, outputs the category and amount to be paid.
a=int(input("enter the shopping amount:"))
d1=(a*20)/100       #d1=discount of gold 
d2=(a*10)/100
d3=(a*5)/100
a1=a-d1             #a1=amount to be paid by gold
a2=a-d2
a3=a-d3
if(a>25000):
    print(f"GOLD\nAmount to be paid = {a1}")
elif(a>10000 and a<25000):
    print(f"SILVER\nAmount to be paid = {a2}")
else:
    print(f"BRONZE\nAmount to be paid = {a3}")




# 4.Design a program in python to display the number of days left in the current year (2019), when 
# today’s date is entered by the user in format of your choice.
a=int(input("enter the day month and year:"))
b=int(input("enter the day month and year:"))
c=int(input("enter the day month and year:"))





# 1.program to print all even number between the given range which are divisible by 6.
a=int (input ("enter the start value range :"))
b=int(input ("enter the stop value range :"))
while(a<b):
    if(a%6==0):
        print(a)
    a=a+1
    


# 2.program to print no. from 100 to 1 in  decending order using for in loop.
for i in range(100,0,-1):
    print(i)

for i in range(1,100,1):        #to print in accending order
    print(i)



# 3.program to print even number between range given range.
a=int(input ("enter the start value (even):"))
b=int (input ("enter the stop value :"))
for i in range(a,b,2):
    print(i)



# 4.program to print the odd number in given range by user.
a=int (input ("enter start value(odd number) :"))
b=int (input ("enter any number for stop value :"))
for i in range (a,b,2):
    print(i)




# LOOP QUESTION
# 1.Program to find whether an entered number is prime or not.
a=int (input ("enter any number to check prime:"))
c=0
i=2
while (i<a):
    if a%i==0:
        c=c+1
        break
    i=i+1
if c==0:
        print("prime")
else:
      print("not prime")



# 2.Program to find the factorial of an entered number.
a=int (input ("enter any number for factorial :"))
for i in range (a,0,-1):
    f=a*i
    print(f"Factorial is = {f}")
    break
    



# 3.program to find the sum of digit of a given number by user.
a=int(input("enter the value of number:"))
sum=0
while(a>0):
    r=a%10
    sum=sum+r
    a=a//10
print(f"Sum of digit is = {sum}")



# 4.program to find the series of all three digits Armstrong numbers.
a=int(input("enter the lower case of armstrong number:"))
b=int(input("enter the upper case of armstrong number:"))
for i in range(a,b,1):
    sum=0
    temp=i
    while (temp>0):
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
        if i==sum:
            print(i)




# PYTHON PROGRAM TO FIND THAT THE GIVEN NUMBER IS ARMSTRONG OR NOT ? 
num = int(input("Enter a number: "))
order = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")





# 5.program to display the table of an entered number in the following format.
#   2*1=2
#   2*2=4
#   .....
#   2*10=20
a=2
for i in range(1,11,1):
    table=a*i
    print(f"2*{i}={table}")







# 1.Program to print the following pattern in python 
#           * * * * *
#           * * * * *
#           * * * * *
#           * * * * *
#           * * * * *
a=int(input ("enter the value row and column:"))
for i in range(a):
    print(a*(' * '))

# alternate method
r=int(input("enter:"))
for i in range(r):
    print(r*(" * "))

#  2.pattern
#       *
#       * *
#       * * *
#       * * * * 
#       * * * * *


# LOOP sheet question
# 1.Print First 10 natural numbers using while loop.
i=1
while i<=10:
    print(i)
    i+=1

# 2.Print the following pattern 
#           1
#           1 2
#           1 2 3
#           1 2 3 4
#           1 2 3 4 5
#           1 2 3 4 5 6




# 3.Calculate the sum of all the number from 1 to given number.
n=int (input("enter :"))
sum =0
for i in range (1,n+1):
    sum =sum+i
print(sum)



# 4.progarm to print the multiplication table of given number.
n=int(input ("enter any integer number: "))
for i in range (1,11):
    table = n*i
    print(f"{n} * {i} = {table}")







# SUM OF TWO NUMBER USING USER DEFINED FUNCTION IN PYTHON ?
def add(x,y):
    sum = x+y
    return sum 
a=int(input("enter : "))
b=int(input("enter : "))
print(f"The sum of the {a} and {b} is = {add(a,b)}")

# OTHER EXAMPLE OF FUNCTION BY MAKING USER DIFINED FUNCTION ?
def f(values):
 values[0] = 44
v = [1, 2, 3]
f(v)
print(v)


# EXAMPLE OF RANDOM.SHUFFLE

import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# SECOND EXAMPLE OF RANDOM.SHUFFLE

import random 
a=["vijay","kumar","gupta"]
random.shuffle(a)
print(a)



# OUTPUT OF THE FOLLOWING PROGRAM
names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
sum = 0
for ls in (names1, names2, names3):
 if ls[0] == 'Alice':
    sum += 1
 if ls[1] == 'Bob':
    sum += 10
print (f"sum is = {sum}")

# OUTPUT == 12




# PYTHON PROGRAM TO TAKE THE NUMEBR OF DAY FROM USER AND TELL HIM THAT HOW MUCH YEAR ,WEAK AND DAY ARE POSSIBLE IN THE GIVEN DAY ?
a=int(input("enter the numeber of day : "))
print(a//365)
print((a%365)//7)
print((a%365)%7)




# python program to make the the login and registration page ?
def login():
    email=input("enter your roll number  :")
    pas=input("enter your passwprd :") 
    ptr = open("vijay.txt",'r')
    a=ptr.read()
    if (email in a and pas in a):
        print("Authentisation successfull")
    else:
        print("login failed")
login()

def register():
    email = input("enter roll : ")
    pas=input("enter pass : ")
    conform=input("conform pass : ")
    ptr = open("vijay.txt",'a')
    ptr.write(email)
    ptr.write(pas)
print("welcome to website please login")
register()





# PYTHON PROGRAM TO CREATE A CAPTCHA CODE IN FRONTENED ONLY ?
import random as r
def captcha():
    text ="abcdefghijklmnopqrstuvwxyz"
    word=r.choice(text)+r.choice(text)+r.choice(text)+r.choice(text)
    print(word)

def login():
    email=input("enter your roll number  :")
    pas=input("enter your passwprd :") 
    ptr = open("vijay.txt",'r')
    a=ptr.read()
    if (email in a and pas in a):
        print("Authentisation successfull")
    else:
        print("login failed")







# 1.write a pthon program to take a number from user and check it is perfect number or not.
n=int(input("enter any number:"))
a=n
sum=0
for i in range (1,(n//2+1)):
    if (a%i)==0:
        sum=sum+i
if sum==a:
    print("perfect number")
else:
    print("not a perfect number")




# 2.program to take a number from user and check it is prime or not.
a=int(input("enter:"))
c=0
for i in range(2,a,1):
    if(a%i)==0:
        c=c+1
if c==0:
    print("prime number")
else:
    print("not a prime number")





# 3.program to take a number from user and check it is armstrong or not.
a=int(input("enter any number:"))
sum=0
l=len(str(a))
for i in str(a):
    sum=sum+(int (i)**l)
if sum==a:
    print("Armstrong")
else:
    print("not Armstrong")

  



# 4.program to take a number from user and find the factorial.
a=int(input("enter any number for factorial:"))
sum=1
for i in range(1,a+1,1):
    sum=sum*i
print(f"Factorial of {a} is = {sum}")




# 5.program to a number from user and check its is strong or not.
a=int(input("enter any number:"))
sum=0
for i in str(a):
    f=1
    for j in range(1,int(i)+1):
        f=f*j
    sum=sum+f
if sum==a:
    print("Strong Number")
else:
    print("Not a Strong number")





# 6 PATTERN:

# 1.   *                     2.           *                   3.     * * * * *                            4.  A
#      * *                              * *                            * * * *                                A B
#      * * *                          * * *                              * * *                                A B C
#      * * * *                      * * * *                                * *                                A B C D
#      * * * * *                  * * * * *                                  *                                A B C D E




# 5.    *               *        6.          *             7.         * * * * * * * * *
#       * *           * *                  * * *                        * * * * * * *
#       * * *       * * *                * * * * *                        * * * * *
#       * * * *   * * * *              * * * * * * *                        * * *  
#       * * * * * * * * *            * * * * * * * * *                        *



# 1.
n=int(input("enter:"))
for i in range(1,n+1):
    print('*'*i)




# 2.
n=int(input("enter:"))
for i in range(1,n+1):
    print(' '*(n-i) + '*'*i)




# 3.
n=int(input("enter:"))
for i in range(n,0,-1):
    print(' '*(n-i) + '*'*i)



# 4.
n=int(input("enter:"))
for i in range(1,n+1):
    print('*'*i + ' '*(2*n-2*i) + '*'*i)



   
# 5.
n=int(input("enter:"))
for i in range (1,n+1):
    for j in range (i):
        print(chr(65+j),end=' ')
    print()



# 6.
n=5
for i in range(1,5):
    for j in range(1,8):
        if(j>=5-i and j<=3+i):
            print('*',end='')
        else:
            print(' ',end='')
    print()


# ALTERNATE METHOD
for i in range (1,6):
    for j in range (5,i,-1):
        print(" ",end = "")
    for k in range(0,i):
        print("* ",end = "")
    print()
 
 


# 7.program to print the pattern of opposite prism .969*r = int (input("enter any number : "))
for i in range (r,1,-1):
    for space in range (0,(r-i)):
        print(" ",end = " ")
    for j in range (i, (2*i - 1)):
        print("*",end = " ")
        for j in range (1,(i-1)):
            print("*",end = " ")
    print()



# ALTERNATE METHOD
for i in range (6,0,-1):
     for j in range (6,i,-1):
         print(" ",end = "")
     for k in range(0,i):
         print(" *",end = "")
     print()





# 1.Write a python program to take a string from user and check it is pangram or not.
s=input("enter the any string : ")
s1=s.lower()
for i in range(97,123):
    if chr(i) not in s1:
        print("Not Pangram")
        break
    else:
        print("Pangram")






# 2.Write a python program to take a string from user and check it is anagram or not.
s1=input("enter string : ")
s2=input("enter string : ")
if (sorted(s1) == sorted(s2) ):
    print("Anagram")
else:
    print("Not Anagram")






# 3.Sorted program with join function.
s=input("enter string : ")
l = sorted(s) 
ll=sorted(s,reverse = True)
print(l)
print(ll)
s1=' '.join(l)
s2=' '.join(ll)
print(s1)
print(s2)




# 4.Program how to print string in python.
s="Abhimanyu"
print(s[2])
print(s[2:7])
print(s[2:])
print(s[:4])
print(s[3::2])
print(s[1:4:3])
print(s[-2:-7:-1])
print(s[ : : ])
print(s[8:2:-1])
print(s[ : :-1])





# 1.WAPP to take a list from user and sum  all its element.
lst = []
n=int(input("enter the list of integer : "))
for i in range (1,n+1):
    lst.append(int(input()))
print(lst)
print(f"Sum of all element is = {sum(lst)}")





# 2.WAPP to take a list from user and make two list one of odd number and one of even number input list in integer format.
lst = []
l1=[]   # l1=list 1
l2=[]   # l2=list 2
n=int(input("enter the number of range : "))
for i in range (1,n+1):
    lst.append(int(input("enter the element : ")))
print(lst)
for i in range (1,n+1):
    if(i%2==0):
        l1.append(i)
    else:
        l2.append(i)
print(f"Even element list : {l1}")
print(f"Odd elemnt list : {l2}")





# 3.WAPP to take two list from user and merge.
l1 = []
l2 = []
lst = []
n=int(input ("enter the range of integer : "))
for i in range (1,n+1):
    l1.append(int(input("enter teh integer : ")))
    l2.append(int(input ("enter for list 2 : ")))

lst =l1 +l2
print(f"Merge of all elemnt from l1 and l2 is = {lst}")






# 4.WAPP to take two list from user and merge them in such a way that resultant list contain no duplicate element.
l1 = []
l2 = []
lst = []
n=int(input ("enter the value of range : "))
for i in range (1,n+1):
    l1.append(int(input("enter the element in list 1 : ")))
    l2.append(int(input("enter the elemnet in list 2 : ")))
lst = l1 + l2
s= set (lst)            # set function is used to not repeat elemnet after merging  
print(f"Merge of both list without duplicate : {s}")



# ALTERNATE METHOD -----WITHOUT TAKING ANOTHER LIST

l= list (map(int ,input() .split( )))
i=0
n= len(l)
while (i<n):
    if l[i] in l[i+1:]:
        del l[i]
        i-=1
        n-=1
    i+=1
print(l)




# 5.WAPP to take a list from user and delete 1st and last occurance of element given by user.
l1 = []
l2 = []
lst = []





# 7.WAPP to find the frequency of each element in a given string .
s = input("enter the element : ")
p = ' '
print("FREQUENCY OF EACH ELEMENT IS :")
for i in s:
    if i not in p:
        print(f"{i} = {s.count(i)}")
        p+=i

# ALTERNATE METHOD

s = input("enter the element : ")
re= ' '
print("FREQUENCY OF EACH ELEMENT IS :")
for i in s:
    if i not in re:
        print(f"{i} = {s.count(i)}")
        re+=i





# 8.PROGRAM TO DELETE THE SAME ITEM IN BOTH THE LIST .
l = list (map(int,input(("enter : ")).split()))
e= int (input ("enter : "))
for i in range (l.count(e)):
    l.remove(e)
print(l)




# 9.WAPP to take a string from user and reverse them .
s = input ("enter : ")
l = s.split()
l.reverse ()
s = ' '.join(l)
print(s)




# 10.WAPP to swap (toggle case) the given string means lower case to upper case and upper case to lower case.
v=str(input("enter any string  : "))
print(v.swapcase())





# 11.WAPP TO TAKE A STRING FROM USER AND MAKE OF ALL VOWEL PRESENT IN THAT STRING USING LIST COMPRIHENSION ?
s=input("enter any string : ")
l=[i for i in s if i in 'aeiouAEIOU']
print(l)


# PYTHON PROGRAM TO MAKE A LIST OF LIST HAVING 3 ELEMENT IN EACH LIST.WHICH SHOWS THE MULTIPLICATION TABLE OF A USER GIVEN INPUT USING LIST COMPRIHENTION ?
n=input("enter any integer : ")
l=[[n,i,n*i] for i in range (1,11)]
for i in l:
    print(l)



# PYTHON PROGRAM TO TAKE 2 LIST FROM USER AND MAKE A LIST OF TUPLE HAVING CORROSPONDING OF BOTH LIST , USING ZIP FUNCTION ?
n=int(input("enter any intiger how much tumpe you need to make : "))
l1=[]
l2=[]
for i in range (n):
    l1.append(input("enter elemnt for frst list : "))
    l2.append(input("enter elemnt for second list : "))
print(l1)
print(l2)
z=zip(l1,l2)
print(list(tuple(z)))




# PYTHON PROGRAM TO TAKE A DITONARIES FROM USER BY TAKING NUMBER OF ELEMENT AND CHECK WHEATHER USER THE GIVEN VALUE ARE PRESENT IN DICTONARIES OR NOT ?
n=int(input("enter : "))
d={}
for i in range(n):
    k=input("enter k : ")
    v=input("enter v : ")
    d[k]=v
print(d)
p=input("enter any value to check : ")
for i in d:
    if p==d[i]:
        print("Present")
        break
else:
    print("Not Present")





# PYTHON PROGRAM TO REVERSE OF TUPLE ?
n=int(input("enter : "))
t=()
for i in range (n):
    element=input("enter element in tupple : ")
    t=t+(element,)
print(t)
l=[]
l=list(tuple(t))
print(l)
l.reverse()
reverse_tupple=tuple(l)
print(reverse_tupple)





# WRITE A PYTHON PROGRAM TO TAKE A N*N MATRIX FROM USER AND PRINT THE SUM OF ITS MINOR DIAGONAL ELEMENTS ?
n=int(input("enter the value of n : "))
matrix = []
print("Enter the matrix elements row by row:")
for i in range(n):
    row = []
    for j in range(n):
        element = int(input("enter : "))
        row.append(element)
    matrix.append(row)

sum_minor_diagonal = 0
for i in range(n):
    sum_minor_diagonal += matrix[i][n - i - 1]

for row in matrix:
    print(row)
print("Sum of minor diagonal elements:", sum_minor_diagonal)





# WRITE A PYTHON PROGRAM TO TAKE A N*N MATRIX FROM USER AND PRINT SUM OF ITS MAJOR DIAGONAL ELEMENTS ?
n=int(input("enter the value of n : "))
matrix=[]
print("enter the elemnet in the matrix")
for i in range(n):
    row = []
    for j in range(n):
        element=int(input("enter : "))
        row.append(element)
    matrix.append(row)
sum_of_major_diagonal_element = 0
for i in range(n):
    sum_of_major_diagonal_element += matrix[i][n+i-3]
for row in matrix:
    print(row)
print(f"Sum of Major diagonal element = {sum_of_major_diagonal_element}")





# WRITE A PYTHON PROGRAM TO TO TAKE A N*N MATRIX FROM USER AND PRINT ITS DIAGONALS ELEMENTS ?
n=int(input("enter the value of n :"))#n=no. of order of square matrix
matrix = []
for i in range (n):
    row = []
    for j in range (n):
        element=int(input("enter : "))
        row.append(element)
    matrix.append(row)
for row in matrix:
    print(row)
M = []
m = []
for i in range (n):
    major_diagonal_element = matrix[i][n+i-3]
    minor_diagonal_element = matrix[i][n-i-1]
    M.append(major_diagonal_element)
    m.append(minor_diagonal_element)
print(f"Major diagonal element = {M}")
print(f"Minor diagonal element = {m}")




# WRITE A PYTHON PROGRAM TO TAKE A M*N MATRIX FROM USER AND PRINT ITS BOUNDARY ELEMENTS ?
m=int(input("enter the row : "))
n=int(input("enter the column : "))
matrix = []
for i in range (m):
    l=list(map(int,input().split()))
    matrix.append(l)
print("Boundary element")
for i in range (m):
    for j in range (n):
        if i==0 or i == m-1 or j==0 or j==n-1:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end = " ")
    print()





# WRITE A PYTHON PROGRAM TO TAKE A M*N MATRIX FROM USER AND PRINT ITS TRANSPOSE ?
matrix = [[5, 4, 3],
          [2, 4, 6],  
          [4, 7, 9],  
          [8, 1, 3]]  
# Define an empty matrix of reverse order  
transpose = [[0, 0, 0, 0],    
             [0, 0, 0, 0],  
             [0, 0, 0, 0]]  
# Use nested for loop on matrix A  
for i in range(4):    
   for j in range(3):    
          transpose[j][i] = matrix[i][j] # store transpose result on empty matrix          
# Printing result in the output  
print("The transpose of matrix  is: ")  
for i in transpose:    
   print(i)




# WRITE A PYTHON SCRIPT TO SORT (ACCENDING AND DECCENDING) A DICTIONARY BY VALUE ?
d= {'apple': 3, 'banana': 1, 'cherry': 2}
# Sort dictionary by value in ascending order
ascending_sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
# Sort dictionary by value in descending order
descending_sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
# Print sorted dictionaries
print("Ascending order:", ascending_sorted_dict)
print("Descending order:", descending_sorted_dict)








# WRITE A PYTHON SCRIPT TO ADD A KEY TO A DICTIONARY ?
n=int(input("enter : "))
d={}
for i in range (n):
    k=input("enter key : ")
    v=input("enter the value of key : ")
    d[k]=v
print("Dictionary is given below : ")
print(d)
d["money"]="life"
print("New Dictionary is given : ")
print(d)





# WRITE A PYTHON PROGRAM TO CONCATENATE FOLLOWING DICTIONARIES TO CREATE A NEW ONE .
# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}

d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d={}
d.update(d1)
d.update(d2)
d.update(d3)
d={**d1,**d2,**d3}
print(d)
# NOTES-** is used to unpaking of the dictionary





# PYTHON PROGRAM TO CHECK IF A GIVEN KEY ALREADY EXISTS IN A DICTIONARY ?
d={"vijay":1,"kumar":2,"3":"gupta"}
k=input("enter the key to check : ")
if k in d:
    print("present")
else:
    print("not present")
    



# PYTHON PROGRAM TO ITERATE OVER DICTIONARIES USING FOR LOOPS ?
n=int(input("enter : "))
d={}
for i in range(n):
    k=input("enter : ")
    v=input("eneter : ")
    d[k]=v
print(d)
# ITERATE THE DICTIONARY BY KEY 
for key in d:
    print(key)
# ITERATE THE DICTIONARY BY VALUE 
for value in d.values():
    print(value)





# PYTHON PROGRAM TO GENERATE AND PRINT THE DICTIONARY THATS CONTAIN A NUMBER (between 1 to n) in form of ( x,x**x ) ?
n=int(input("enter : "))
d={}
for i in range (1,n+1):
    d[i]=i*i
print(d)
    




# PYTHON PROGRAM TO PRINT A DICTIONARY WHERE KEY ARE THE NUMBER BETWEEN THE (1 to 15 ) AND BOTH THE NUMBER IN RAANGE ARE INCLUDED AND THE VALUES ARE THE SQUARE OF TH KEY 
n=16
d={}
for i in range (1,n):
    d[i]=i**2
print(d)





# PYTHON PROGRAM TO MERGE THE TWO PYTHON DICTIONARY ?
d={}
d1={"vijay":1,"kumar":2}
d2={"gupta":3}
d1.update(d2)
print(d1)





# PYTHON PROGRAM TO SUM ALL THE ELEMENT IN A DICTIONARY ?
d={"vijay":4,"kumar":9,"gupta":6}
sum=0
for value in d.values():
    sum+=value
print(f"Sum of all the element is = {sum}")





# Write a program To take number of pens in a bucket from user and find That In how many ways we can pick pens from bucket so that no pen left in bucket. 
# Note: if you pick i pens in first chance then you have to pick i pens in all left chances.

# Sample input 1:
# 12
# Sample output 2:
# 6 ways

# Sample input 2:
# 25
# Sample output 2:
# 3 ways

n=int(input("enter : "))
c=0
for i in range (1,n+1):
    if n%i==0:
        c+=1
print(c)




# PYTHON PROGRAM TO FIND THE CALENDER OF GIVEN MONTH AND YEAR ?
import calendar 
year=int(input("enter the year : "))
month=int(input("enter the month  : "))
print(calendar.month(year,month))




# PYTHON CODE TO FIND THE OUTPUT OF FOLLOWING ?
a=20
def f():
    a=15
    print(a)    # 15
    a=10
    print(a)    # 10
    def t():
        global a
        a=5
        print(a)    # 5
    t()
    print(a)    # 10
    def g():
        nonlocal a
        a=7
        print(a)    # 7
    g()
    print(a)    # 7
f()
print(a)    # 5





# Example of lamda function ?
double = lambda x: x * 2
print("OUTPUT")
print(double(5))




# EXAMPLE OF LAMDA FUNCTION ?
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) ,my_list)) 
print(new_list)     #[4,6,8,12]




# Write a function to calculate area and perimeter of a rectangle ?
def area(l,b):
    return (l*b)

def perimeter(l,b):
    return (2*(l+b))

l=int(input("enter the length of rectangle : "))
b=int(input("enter teh breath of rectangle : "))
print(f"Length = {l}\nBreath = {b}")
print(f"Area = {area(l,b)}")
print(f"Perimeter = {perimeter(l,b)}")





# Write a function to calculate the area and the circumference of the circle ?
def area(r,pi=3.14):
    return (pi*r*r)
def circumfernce(r,pi=3.14):
    return (2*pi*r)

r=int(input("enter the radius of circle : "))
print(f"Radius,r={r}")
print(f"Area of circle = {'%.2f'%(area(r,pi=3.14))}")
print(f"Circumfernce of circle = {'%.2f'%(circumfernce(r,pi=3.14))}")






# Write a function to tell user if he/she is able to vote or not.
def vote(n,a):
    print(f"{n} you are able to vote")
    print(f"THANK YOU {n}")
def notvote(n,a):
    print(f"Sorry {n} you are not able to vote")

n=input("enter your Name : ")
a=int(input("enter your age : "))
if a>=18:
    vote(n,a)
else:
    notvote(n,a)
    r=18-a
    print(f"After {r} year you can vote\nTHANK YOU")







# Write a function to check if a number is prime or not ?
def prime(n):
    c=0
    for i in range(2,n,1):
        if (n%i)==0:
            c+=1
    if c==0:
        print(f"{n} is prime number")
    else:
        print(f"{n} is Not Prime number")
n=int(input("enter : "))
prime(n)






# WRITE A PYTHON PROGRAM TO WRITE A FILE NAMED ABC.TXT AND WRITE ANY FIVE  LINE IN THAT FILE ?
f=open("abc.txt",'w')
f.write("hello how are you \ni am fine\n")
l=["vijay\n","kumar\n","gupta\n"]
f.writelines(l)
f.close()
f=open("abc.txt",'r')
g=f.read()
print(g)





# PYTHON PROGRAM TO TAKE  A INPUT IN FILE HANDLING AND PRINT IN THE THE .TEXT FILE ?
f=open("vijay.txt",'w')
n=int(input("enter the number of line : "))
for i in range (n):
    s=input("enter : ")+"\n"
    f.write(s)






# WRITE A PYTHON PROGRAM TO COUNT NUMBER OF WORD AND NUMBER OF LINE IN A TEXT FILE ?
print()
print("\t----WRITE IN FILE USING PYTHON----\t")
print()
f=open("vijay.txt",'w')
n=int(input("enter the no. of inputs: "))
for i in range(n):
    s=input("enter : ")+"\n"
    f.write(s)

#open file in program
f= open("vijay.txt",'r')
wordsList=(f.read().split())
lenWordsList = len(wordsList)
print("NUMBER OF WORDS IN THE FILE =",lenWordsList)

#count characters in files
countCharacters=0
for word in wordsList:
    lenWord= len(word)
    countCharacters +=lenWord
print("NUMBER OF CHARACTERS IN THE FILE =",countCharacters)
f.seek(0)

#count lines in files
f=open("vijay.txt","r")
linesList = f.read().split("\n")
countLinesList= len(linesList)-1
print("NUMBER OF LINES IN FILE =",countLinesList)
f.seek(0)






# USE OF RANDOM FUNCTION
from random import*
n1=randint(5,50)
print(n1)
n2=randrange(5,100,2)
print(n2)
n3=random()
print(n3)
n4=uniform(10,30)#will give a floating point number 
print(n4)


# USE OF RANDOM FUNCTION 
from random import*
l=["hello",5,7.5,"by",2,(7,3,9)]
seed(9) # SEED IS USE TO FIX RANDOM VALUE FOR ALL THE SYSTEM IN THE RANDOM FUNCTION 
n1=randint(5,40)
print(n1)
n2=randrange(5,100,2)
print(n2)
n3=random()    # will give a random value between 0-1 i.e floating number
print(n3)
n4=uniform(10,30)   # give a random floating number between the range 
print(n4)
n5=choice(l)
print(n5)
n6=choices(l,k=4)
print(n6)   # list of 4 element from list l3
print(l)
shuffle(l)  # USE TO REVERSE THE LIST IN RANDOM FUNCTION 
print(l)
# GIVE THE NUMBER OF BITS BETWEEN THE 0-63
n7=getrandbits(4)
print(n7)
n8=getrandbits(6)
print(n8)




# WRITE A PYTHON PROGRAM TO GENERATE A RANDOM PASSWORD OF NUMBER OF CHARACTER OF LENGTH PASSWORD MUST CONTAIN ATLEAST ONE LOWER CASE AND ONE UPPER CASE AND DIGIT AND ONE SPECIAL CHARACTER (#,@'.'','';')
from random import*
n=int(input("enter the length of password : "))
p=""
s=[]
l1=["v","i","j","a","y"]
l2=["K","U","M","A","R"]
l3=["@","#",".",",",";"]
for i in range((n//3)):
    s.append(choice(l1))
    s.append(choice(l2))
    s.append(choice(l3))
print(s)
print("YOUR PASWORD IS BELOW GIVEN BELOW :")
for i in s:
    p+=str(i)
print(p)

# ALTERNATE METHOD
from random import*
n=int(input("enter : "))
l=[]
s=""
l1=['@','#','.',"'",';']
l2=[l.append(i) for i in range(0,10)]
l3=[l.append(chr(i)) for i in range(65,91)]
l4=[l.append(chr(i)) for i in range(97,123)]
p=choices(l,k=n)
print(p)
for i in p:
    s+=str(i)
print(s)





# WRITE A PYTHON PROGRAM TO MAKE A GAME HAVING 3 LEVELS IN GAME USER HAVE TO GAUSE A NUMBER WITHIN RANGE PROVIDED BY PROGRAMMER IF USER GAUSE 
# THE RANDOM NUMER SELECTED BY THE PROGRAMMER THEN HE WIN OTHER WISE HE LOSS YOU CAN ALSO HINT THE USER 
# IN LEVEL 1 USER WILL GET 20 CHANCES IN LEVEL 2 USER GET 10 CHANCS 
# IN 3RD LEVEL USER WILL GET 10 SECOND

from random import*
import time
n=time.time() #second from 1st january 1970 to system current time 
l=[]
while time.time()-n<10:
    s=input()
    l.append(s)
print(l)




# EXAMPLE OF LIST COMPRIHENSION 
s='how world how are you'.split()
l=[i if i!='how' else 'hello' for i in s]
print(l)





# 1. Write a Python program that takes a list of numbers as input and returns the sum of all even numbers in the list. 
n=int(input("enter : "))
l=[]
for i in range(n):
    l.append(int(input("enter number : ")))
print(l)
sum =0
for i in l:
    if(i%2==0):
        sum+=i
print(f"sum of all even number in list :{sum}")




# 2. Write a Python program that takes a string as input and returns the number of vowels in the string.
print()
s=input("ENTER THE STRING : ")
n=len(s)
print(f"LENGTH OF STRING :{n}")
c=0
l=[]
v="AaEeIiOoUu"
for i in s:
    if i in v:
        c+=1
        l.append(i)
print(f"NO OF VOWELS IN STRING :{c}")
print(f"VOWEL PRESENT IN STRING :{l}")


# 3. Write a Python program that takes two lists as input and returns a new list that contains the common elements of both lists.
l1=[]
l2=[]
l3=[]
l1=input("enter : ")
l2=input("enter : ")
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)


# 4- Write a Py`thon program that takes a number as input and returns True if it is a prime number, and False otherwise.
n=int(input("enter : "))
c=0
for i in range(2,n,1):
    if n%i==0:
        c+=1
if c==0:
    print("TRUE")
else:
    print("FALSE")


# 5. Write a Python program that takes a list of integers as input and returns the largest number in the list(without using max()).
def largestnumber(n):
    largest =n[0]
    for i in n:
        largest =i
    return largest
n=[10,46,12,56,78]
print(n)
largest =largestnumber(n)
print(f"YOUR LARGEST NUMBER IS {largest}")


# ALTERNATE METHOD
n=int(input("enter : "))
l=[]
for i in range (1,n+1):
    l.append(int(input("enter:")))
    largest_number =max([i for i in l])
print(f"LARGEST NUMBER IN THEE LIST IS :{largest_number}")




# 5- Write a Python program that asks the user for a number 
# and then displays the multiplication table for that number 
# (up to 10) using list comprehension.
print()
n=int(input("enter table name : "))
print()
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
print()

# ALTERNATE METHOD
print()
n=int(input("enter table name:"))
print()
Table=[(i*n) for i in range(1,11)]
print(Table)


# 6- Write a program to find the GCD of two numbers.
# GCD (a, b) = (a × b)/ LCM (a, b).     GCD or HCF = GREATEST COMMON DIVISION both are same but differnt 
print()
a=int(input("enter the 1st number : "))
b=int(input("enter the 2nd number : "))
if a>b:
    small=b
else:
    small=a
for i in range(1,small+1):
    if a%i==0 and b%i==0:
        hcf=i
print(f"THE GCD ={hcf}")
print()



# 7- Write a program to find the LCM of two numbers. 
print()
a=int(input("enter the 1st number : "))
b=int(input("enter the 2nd number : "))
if a>b:
    big=a
else:
    big=b
while True:
    if big % a==0 and big % b==0:
        lcm=big
        break
    big+=1
print(f"THE LCM ={lcm}")



# 8- Write a program to convert a decimal number to binary 
# with and without bin().
a=int(input("enter the float number :"))
b=bin(a)[2:]
print(b)

# ALTERNATE METHOD
a=int(input("enter any number : "))
b=''
while a>0:
    r=a%2
    b=str(r)+b
    a//=2
print(b)


# 9- Write a program to check if a given string is a valid email address or not. 
print()
s=input("enter email id : ")
print(s)
print()
if'@' and '.com'in s:
    print("VALID")
else:
    print("INVALID")
print()




# 10-Write a program to check if a given number is an Armstrong number or not.
print()
n=int(input("enter:"))
sum =0
order = len(str(n))
temp=n
while temp>0:
    digit=temp%10
    sum=sum+digit**order
    temp=temp//10
if sum == n:
    print(f"{n} is Armstrong Number")
else:
    print(f"{n} in NOt an Armstrog number")
print()