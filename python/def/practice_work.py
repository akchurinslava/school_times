#1
from my_module2 import *
a=arithmetic(2.5,1.8,"+")
print(a)
while True:
    try:
        a=arithmetic(input(),input(),input())
        print(a)
        break
    except:
        print('Enter correct data')


#2
from my_module2 import *

while True:
    try:
        a=is_year_leap(int(input()))
        print(a)
        break
    except:
        print('Enter correct data')

#3
from my_module2 import *
from math import *

while True:
    try:
        a=square(input())
        print(a)
        break
    except:
        print('Enter correct data')

#4
from my_module2 import *

while True:
    try:
        a=season(input())
        print(a)
        break
    except:
        print('Enter correct data')

#5
from my_module2 import *

while True:
    try:
        a=bank(input(), input())
        print(a)
        break
    except:
        print('Enter correct data')

#6
from my_module2 import *

while True:
    try:
        a=is_prime(input())
        print(a)
        break
    except:
        print('Enter correct data')

#7
from my_module2 import *

while True:
    try:
        a=date(input(),input(),input())
        if a!=None:
            print(a)
        break
    except:
        print('Enter correct data')


#8
from my_module2 import *

while True:
    try:
        a=XOR_cipher(input(), special_key(input()))
        print(a)
        break
    except:
        print('Enter correct data')

while True:
    try:
        b=XOR_uncipcher(input(), special_key(input()))
        print(b)
        break
    except:
        print('Enter correct data')