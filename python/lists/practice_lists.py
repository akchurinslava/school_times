#task 1
from math import *
from random import *


while True:
	a=input('Enter post index:')
	if a.isdigit() and len(a)==5:
		b=list(a)
		c=b[0]
		break
if c=='1':
	print('Location - Tallinn')
	print('Stay at home')
elif c=='2':
	print('Location - Narva, Narva-Joesuu')
	print('Stay at home')
elif c=='3':
	print('Location - Kohtla-Jarve')
	print('Stay at home')
elif c=='4':
	print('Location - Ida-Virumaa, Jogevamaa')
	print('Wear a mask')
elif c=='5':
	print('Location - Tartu linn')
	print('Wear a mask')
elif c=='6':
	print('Location - Tartumaa, Polvamaa, Vorumaa, Valgamaa')
	print('Wear a mask')
elif c=='7':
	print('Location - Viljandimaa, Jarvamaa, Harjumaa, Raplamaa')
	print('Wear a mask')
elif c=='8':
	print('Location - Parnumaa')
	print('Wear a mask')
else:
	c=='9'
	print('Location - Laanemaa, Hiiumaa, Saaremaa')
	print('Wear a mask')

#task2 version1
from math import *
from random import *


a=list(map(int, input('Please enter list separated by [,]:').split(',')))
b=int(input('Enter how much times we are doing a castling of the letter:'))
c=-1

for i in range(b):
	a[i], a[c]=a[c], a[i]
	c-=1
print(a)


#task2 version2
from math import *
from random import *


a=[1,2,3,4,5,6,7,8]
b=int(input('Enter how much times we are doing a castling of the letter:'))
c=-1

for i in range(b):
	a[i], a[c]=a[c], a[i]
	c-=1
print(a)



#task3
from math import *
from random import *

a=input('Enter list, separate by [,]:').split(',')
b=max(a)
c=len(a)
ac=a.index(b)
abc=int(b)/int(c)
a[ac]=abc

print(a)


#task4
from math import *
from random import *

a=list(map(int, input('Please enter list separated by [,]:').split(',')))


b=input('What you want to do, sort from smallest to biggest - 1\nor from biggest to smallest - 2:')

if b=='1':
	a.sort()
	print(a)
elif b=='2':
	a.sort(reverse=True)
	print(a)
else:
	print('Only 1 or 2')

#task4 version2
from math import *
from random import *

a=input('Please enter list separated by [,]:').split(',')


b=input('What you want to do, sort from smallest to biggest - 1\nor from biggest to smallest - 2:')

if b=='1':
	a.sort(key=int)
	print(a)
elif b=='2':
	a.sort(key=int, reverse=True)
	print(a)
else:
	print('Only 1 or 2')

#task4 version3
from math import *
from random import *

a=sorted(input('TEST:').split(','),key=int)

b=input('What you want to do, sort from smallest to biggest - 1\nor from biggest to smallest - 2:')

if b=='1':
	print(a)
elif b=='2':
	c.sort(reverse=True)
	print(a)
else:
	print('Only 1 or 2')

#task5

from math import *
from random import *


list1=['fdsfdsfs', 'dsgevdfv', 'gdfgdfccsd']
list2=['fdsapwqesfs', 'dsvdfv', 'dfccsd']
list3=['fdss', 'dvdfv', 'gmnbnvbfccsd']

print([x.ljust(len(max(list1, key = len)), '_') for x in list1])
print([x.ljust(len(max(list2, key = len)), '_') for x in list2])
print([x.ljust(len(max(list3, key = len)), '_') for x in list3])




#task6

from math import *
from random import *

while True:
	a=input('Enter your name:')
	if a.isalpha():
		list(a)
		break
c=str.capitalize(a)
print('Hello ' + c +' !')
b=len(a)
print('Your name content '+str(b)+' letters')
vowel=0
consonants=0
all_vowel=['a','e','i','o','u']
for i in a:
	if i in all_vowel:
		vowel+=1
	else:
		consonants+=1
print('In your name '+str(vowel)+ ' vowel letters!')
print('In your name '+str(consonants)+ ' consonant letters!')
q=sorted(list(a),key=str)
q_true=[]
for i in q:
	if i not in q_true:
		q_true.append(i)

print(str(q_true))
