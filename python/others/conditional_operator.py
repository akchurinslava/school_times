

#NR 1
a=float(input('Enter number:'))
if a>0:
	if a%2==0:
			print(f'{a} is an even number')
	else:
		print(f'{a} odd number')
else:
	print('Does not work')

#NR2

a=float(input('Number1 :'))
b=float(input('Number2 :'))
c=float(input('Number3 :'))
if a>0 and b>0 and c>0:
	if a+b+c==180:
		if a==b==c==60:
			print('equilateral triangle')
		elif a==b or b==c or a==c:
			print('Isosceles triangle')
		else:
			print('Versatile triangle')
	else:
		print('Not triangle')
else:
	print('Not correct')

#NR3
d=input('Do you want decoding [Yes or No]:')
if d.upper()=="YES":
	number=int(input('Choose number from 1 to 7:'))
	if number==1:
		day="Monday"
	elif number==2:
		day="Tuesday"
	elif number==3:
		day="Wednesday"
	elif number==4:
		day="Thursday"
	elif number==5:
		day="Friday"
	elif number==6:
		day="Saturday"
	elif number==7:
		day="Sunday"

	print(str(number)+ f' is {day}')
else:
	print(str('bye'))


#NR4

a=int(input('Enter day:'))
b=int(input('Enter month:'))
if a>0 and b>0 and a<=31 and b<=12:
	if a>=21 and a<=31 and b==3 or a>=1 and a<=20 and b==4:
		sign="Aries"
	elif a>=21 and a<=31 and b==4 or a>=1 and a<=21 and b==5:
		sign="Taurus"
	elif a>=22 and a<=31 and b==5 or a>=1 and a<=21 and b==6:
		sign="Gemini"
	elif a>=22 and a<=31 and b==6 or a>=1 and a<=22 and b==7:
		sign="Cancer"
	elif a>=23 and a<=31 and b==7 or a>=1 and a<=21 and b==8:
		sign="Leo"
	elif a>=22 and a<=31 and b==8 or a>=1 and a<=23 and b==9:
		sign="Virgo"
	elif a>=24 and a<=31 and b==9 or a>=1 and a<=23 and b==10:
		sign="Libra"
	elif a>=24 and a<=31 and b==10 or a>=1 and a<=22 and b==11:
		sign="Scorpio"
	elif a>=23 and a<=31 and b==11 or a>=1 and a<=22 and b==12:
		sign="Saggitarius"
	elif a>=23 and a<=31 and b==12 or a>=1 and a<=20 and b==1:
		sign="Capricorn"
	elif a>=21 and a<=31 and b==1 or a>=1 and a<=19 and b==2:
		sign="Aquarius"
	elif a>=20 and a<=31 and b==2 or a>=1 and a<=20 and b==3:
		sign="Pisces"
	print('Your sign is ' + sign)
else:
	print('Incorrect data')


#NR5


from math import *
a=input('Enter value:')
if a.isalnum():
	if a.isdigit():
		c=int(a)/2
		print(c)
	elif a.isalpha():
		print(a)
else:
	a==float
	print(float(a)*0.7)



#NR6

from math import *
a=float(input('Please enter the number for A:'))
b=float(input('Please enter the number for B:'))
c=float(input('Please enter the number for C:'))
if a!=0:
	d=b*b-4*a*c
	if d<0:
		print('No solutions')
	elif d>0:
		x1=(-b+sqrt(d))/2*a
		x2=(-b-sqrt(d))/2*a
		print('x1='+str(round(x1,2))+' x2='+str(round(x2,2)))
	elif d==0:
		x3=-b/(2*a)
		print(str(round(x3,2)))
else:
	print("A can't be 0")








