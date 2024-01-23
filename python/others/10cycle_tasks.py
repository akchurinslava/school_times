

#Task1
j=0
i=0
while True:
	i+=1
	a=float(input(f'{i} Enter A: '))
	if int(a)==a:
		j+=1
	if i==15: break
print(j)
#Task2
from math import *
c=int(input('Enter a number:'))
a=0
for x in range(1,c+1):
	a=x+a
print(a)
#Task3
x=1
z=1
for i in range(0,8,1):
	x =float(input('Enter a number:'))
	if x>0:
		z*= x
print(z)
#Task4
for i in range(10,20):
	print(i**2)	
#Task5
n=int(input('Enter quantity of N:'))
z=0
for i in range(0,n,1):
	x =float(input('Enter a number:'))
	if x<0:
		z+=x
print(z)
#Task6
n=int(input('Enter quantity of N:'))
z=0
q=0
y=0
l=0
for i in range(0,n,1):
	x =float(input('Enter a number:'))
	if x<0:
		q+=1
	elif x>0:
		y+=1
	else:
		x=0
		l+=1
print('The number of negativa',q)
print('The numbet of positive',y)
print('The number of zeros',l)
#Task7
z=int(input('Enter a multiplicity:'))
a=int(input('Enter a A:'))
b=int(input('Enter a B:'))
for i in range(a, b+1, 1):
	if i%z==0:
		print(int(i))
#Task8
for i in range(1, 20):
	i=float(i*2.5)
	print(str(i))
#Task9
n=int(input('Deposit:'))
s=int(input('Years:'))
z=0
for i in range(s*12):
	z=n*0.03/12
	n+=z
	output=n
print(output)
#task10!!!
z=0
while z!=10:
	z+=1
	a,b=map(int,input(f'Pair{z}: ').split())
	if a==0 and b==0:break
	else:
		if a>b:
			print(a)
		elif a<b:
			print(b)
#task10 v2
from math import *
from random import *
text=''
for i in range(1, 11):
	a1=randint(-100,100)
	a2=randint(-100,100)
	if a1>a2:
		print(f'{a1} is bigger then {a2}')
	elif a2>a1:
		print(f'{a2} is bigger then {a1}')
	else:
		print(f'{a1} and {a2} are equal')
print(text)
#task11
from random import *
y = 1
a=(randrange(1, 100))
for i in range(1, 100):
    if i%2 == 1:
        if i%a == 0:
            y *= i
print(y)
#task12!!!!
a=int(input('Enter number of lawn mowers:'))
b=int(input('Hours of first lawn mower worked:'))
c1=b*60
for i in range(1, a):
	c1+=10
print(c1)
#task12 v2
n=int(input('Number of ***'))
m=int(input('Min'))
m*=60
summ=0

for i in range(1, n):
	summ+=m
	m+=10
print(m)
#task13
j=0
summ=0
for i in range(105, 1001,7):
	summ+=i
	j+=1
print(j)
print(summ)
#task14
a=int(input('Enter N value:'))
b=1
for i in range(1, a):
	b*=i
print(b)
#task15
j=0
while True:
	j+=1
	print('0 1 2 3 4 5 6 7 8 9')
	if j==10:break
#task16!!!!!
for r in range(9):
	for i in range(9):
			if r==c:
				print(r+1, end='')
			else:
				print(0,end='')
	print()
#task17
a=2
i=1
i_2=0
c=0
while True:
	c+=1
	i_2+=i
	y=a*i_2
	if c==9:break
	print(str(a) + '*'+str(i_2)+ '=' +str(y))
#task18
for i in range(20, 51):
	if i%3==0 and i%5!=0:
		print(i)
#task19
for i in range(35, 87):
	if i%7==1 and i%7==2 or i%7==5:
		print(i)
#task20
a=0
for i in range(1, 50):
	if i%7==0 or i%5==0:
		a+=i
print(a)
#task21!!!
q=0
while q!=10:
	q+=1
	i=int(input(f"Enter number {q}:"))
	if i<0:
		b=abs(i)
		print(b)
	else:
		print(i)
#task22
a=0
for i in range(100, 201):
  if i%17==0:
    a+=i
print(a)
#task23 !!!!

#task24
y=[]
a=int(input('Enter number of students:'))
j=0
for i in range(1, a+1):
  j+=1
  b=int(input(f'Enter {j} student height:'))
  y.append(b)
  c=sum(y)
  c1=c/a
print(c1)
#task25
y=[]
a=int(input('Enter a number:'))
for i in range(1, a+1):
  if a>0:
    if i%2!=0 and i%3!=0 and i%5!=0:
      y.append(i)
      c=len(y)
print(c)
#task26
a=input('Enter two two-digit number one after other:')
b=(a[0:2])
c=(a[2:4])
b1=int(b)
c1=int(c)
a1=int(a)

y=a1/(b1*c1)
print(y)

#task27

















