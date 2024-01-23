#version 1

from math import *
from random import *
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLACK)
print(Back.GREEN)

a=input('Please choose your level[easy, normal, hard]:')
print(Back.CYAN)
if a.lower() == 'easy':
    print('So you chose a newbie level')
    print('You do not have to be great to start, but you have to start to be great...')
    input('Please press enter to continue...')
    c1=0
    c2=0
    for i in range(5):
        n1=randint(1, 100)
        n2=randint(1, 100)
        action=randint(1, 50)
        if action<=25:
            a1=int(input(str(n1)+'+'+str(n2)+'='))
            check=n1+n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        else:
            action>25
            a1=int(input(str(n1)+'-'+str(n2)+'='))
            check=n1-n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
elif a.lower() == 'normal':
    print('So you chose an amateur level')
    print('A samurai has no goal, only a path...')
    input('Please press enter to continue...')
    c1=0
    c2=0
    for i in range(10):
        n1=randint(1, 100)
        n2=randint(1, 100)
        action=randint(1, 75)
        if action<=25:
            a1=int(input(str(n1)+'+'+str(n2)+'='))
            check=n1+n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        elif action<=50:
            a1=int(input(str(n1)+'-'+str(n2)+'='))
            check=n1-n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        else:
            action>50
            a1=int(input(str(n1)+'*'+str(n2)+'='))
            check=n1*n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
elif a.lower() == 'hard':
    print('So you chose a pro level')
    print('The winners never quit and quiters never win...')
    input('Please press enter to continue...')
    c1=0
    c2=0
    for i in range(10):
        n1=randint(1, 100)
        n2=randint(1, 100)
        action=randint(1, 125)
        hard=randint(1, 30)
        if action<=25:
            a1=int(input(str(n1)+'+'+str(n2)+'='))
            check=n1+n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        elif action<=50:
            a1=int(input(str(n1)+'-'+str(n2)+'='))
            check=n1-n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        elif action<=75:
            a1=int(input(str(n1)+'*'+str(n2)+'='))
            check=n1*n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        elif action<=100:
            a1=int(input(str(n1)+'/'+str(n2)+'='))
            check=n1/n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        else:
            action>100
            if hard<10:
                a1=int(input(str(n1)+'**'+'2'+'='))
                check=n1**2
                if check==a1:
                    c1+=1
                else:
                    check!=a1
                    c2+=1
            elif hard<20:
                a1=int(input(str(n1)+'**'+'3'+'='))
                check=n1**3
                if check==a1:
                    c1+=1
                else:
                    check!=a1
                    c2+=1
            else:
                hard>20
                a1=int(input(str(n1)+'**'+'4'+'='))
                check=n1**4
                if check==a1:
                    c1+=1
                else:
                    check!=a1
                    c2+=1
else:
    print('Please enter correct easy or normal or hard')
print(Fore.RED)
print(Back.RESET)
if c1==0:
    print('Your grade is 1')
elif c2==0:
    print('RAMPAGE')
elif c1/c2*100<60:
    print('Your grade is 2')
elif c1/c2*100>=60 and c1/c2*100<=75:
    print('Your grade is 3')
elif c1/c2*100>=75 and c1/c2*100<=90:
    print('Your grade is 4')
else:
    c1/c2*100>90
    print('Your grade is 5')



#version2


from math import *
from random import *
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLACK)
print(Back.GREEN)

a=input('Please choose your level[easy, normal, hard]:')
print(Back.CYAN)
if a.lower() == 'easy':
    print('So you chose a newbie level')
    print('You do not have to be great to start, but you have to start to be great...')
    input('Please press enter to continue...')
    print()
    c1=0
    c2=0
    for i in range(5):
        n1=randint(1, 100)
        n2=randint(1, 100)
        action=randint(1, 50)
        if action<=25:
            a1=int(input(str(n1)+'+'+str(n2)+'='))
            check=n1+n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        else:
            action>25
            a1=int(input(str(n1)+'-'+str(n2)+'='))
            check=n1-n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
    print(Fore.RED)
    print(Back.RESET)
    if c1==0:
        print('Your grade is 1')
    elif c2==0:
        print('RAMPAGE')
    elif c1/c2*100<60:
        print('Your grade is 2')
    elif c1/c2*100>=60 and c1/c2*100<=75:
        print('Your grade is 3')
    elif c1/c2*100>=75 and c1/c2*100<=90:
        print('Your grade is 4')
    else:
        c1/c2*100>90
        print('Your grade is 5')
elif a.lower() == 'normal':
    print('So you chose an amateur level')
    print('A samurai has no goal, only a path...')
    input('Please press enter to continue...')
    print()
    c1=0
    c2=0
    for i in range(10):
        n1=randint(1, 100)
        n2=randint(1, 100)
        action=randint(1, 75)
        if action<=25:
            a1=int(input(str(n1)+'+'+str(n2)+'='))
            check=n1+n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        elif action<=50:
            a1=int(input(str(n1)+'-'+str(n2)+'='))
            check=n1-n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        else:
            action>50
            a1=int(input(str(n1)+'*'+str(n2)+'='))
            check=n1*n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
    print(Fore.RED)
    print(Back.RESET)
    if c1==0:
        print('Your grade is 1')
    elif c2==0:
        print('RAMPAGE')
    elif c1/c2*100<60:
        print('Your grade is 2')
    elif c1/c2*100>=60 and c1/c2*100<=75:
        print('Your grade is 3')
    elif c1/c2*100>=75 and c1/c2*100<=90:
        print('Your grade is 4')
    else:
        c1/c2*100>90
        print('Your grade is 5')
elif a.lower() == 'hard':
    print('So you chose a pro level')
    print('The winners never quit and quiters never win...')
    input('Please press enter to continue...')
    print()
    c1=0
    c2=0
    for i in range(10):
        n1=randint(1, 100)
        n2=randint(1, 100)
        action=randint(1, 125)
        hard=randint(1, 30)
        if action<=25:
            a1=int(input(str(n1)+'+'+str(n2)+'='))
            check=n1+n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        elif action<=50:
            a1=int(input(str(n1)+'-'+str(n2)+'='))
            check=n1-n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        elif action<=75:
            a1=int(input(str(n1)+'*'+str(n2)+'='))
            check=n1*n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        elif action<=100:
            a1=int(input(str(n1)+'/'+str(n2)+'='))
            check=n1/n2
            if check==a1:
                c1+=1
            else:
                check!=a1
                c2+=1
        else:
            action>100
            if hard<10:
                a1=int(input(str(n1)+'**'+'2'+'='))
                check=n1**2
                if check==a1:
                    c1+=1
                else:
                    check!=a1
                    c2+=1
            elif hard<20:
                a1=int(input(str(n1)+'**'+'3'+'='))
                check=n1**3
                if check==a1:
                    c1+=1
                else:
                    check!=a1
                    c2+=1
            else:
                hard>20
                a1=int(input(str(n1)+'**'+'4'+'='))
                check=n1**4
                if check==a1:
                    c1+=1
                else:
                    check!=a1
                    c2+=1
    print(Fore.RED)
    print(Back.RESET)
    if c1==0:
        print('Your grade is 1')
    elif c2==0:
        print('RAMPAGE')
    elif c1/c2*100<60:
        print('Your grade is 2')
    elif c1/c2*100>=60 and c1/c2*100<=75:
        print('Your grade is 3')
    elif c1/c2*100>=75 and c1/c2*100<=90:
        print('Your grade is 4')
    else:
        c1/c2*100>90
        print('Your grade is 5')

else:
    print('Please enter correct easy or normal or hard')