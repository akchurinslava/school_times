def arithmetic(a1:float,a2:float,sym:str):
    """Easy calculator
    + -, - -. * multiple, / split
    :param float a1: First number
    :param float a2: Second number
    :param str sym: Doing
    :rtype: var unknown format
    """
    if sym in ["+","-","/","*"]:
        if sym=='/' and a2==0:
            answ='Div/0'
        else:
            answ=eval(str(a1)+sym+str(a2))
    else:
        answ="Uknown move!"
    return answ

def is_year_leap(a:int):
    """
    Leap year or not
    insert year to check it
    :param int
    :param b bool
    :rtype: bool
    """
    a=int(a)
    if a%4==0:
        b=True
    else:
        b=False
    return b

from math import *
def square(a:float):

    """
    insert square side
    give back Psquare, Ssquare, dSquare
    :param float
    :rtype:float
    """
    a=float(a)
    Psquare=a*4
    Ssquare=a*a
    dSquare=sqrt(a)
    return Psquare, Ssquare, dSquare

def season(a:int):
    """
    insert month number
    give back year season of that month.
    :param int
    :rtype: str
    """
    a=int(a)
    if a in range(3,6):
        a="Spring"
    elif a in range(6,9):
        a="Summer"
    elif a in range(9,12):
        a='Autumn'
    elif a==12 or a==1 or a==2:
        a='Winter'
    else:
        print('Not correct month number')
    return a

def bank(a:float, years:int):
    """
    Bank interest rates function
    return summ with percents
    :param a float: start summ
    :param years int: for how many years
    :rtype: float
    """
    a=float(a)
    years=int(years)

    S=a*(1+0.1)**years
    return S

def help_is_prime(a:int):
    """
    This is small script help us make task 6
    Calculate zeros and return to us answer if zeros>2 - False
    :param int a: input number
    :param int b: calculated zeros
    :param bool c: returned value
    :rtype: bool
    """
    a=int(a)
    b=0
    for i in range(2, a+1):
        if a%i==0:
            b+=1
            if b>2:
                c=False
            else:
                c=True
    return c

def is_prime(a:int):
    """
    Enter number from 0 to 1000
    Here we use help module named "help_is_prime()" for info check it above
    Return True if prime number and False if not
    :param int a: entered number
    :param bool b: returned value
    :rtype: bool
    """
    a=int(a)
    if a>=0 and a<=1000:
        b=help_is_prime(a)
    else:
        b=('Incorrect number')
    return b


def help_date(a:int, b:int, c:int):
    """
    This is small support script for "def date()"
    Help calculate leap year
    Return True or False
    :param int a,b,c: day,month,year
    :param bool answ: returned value
    :rtype: bool
    """
    if c%4==0 and b==2 and a<=29:
        answ=True
    elif c%4!=0 and b==2 and a<=28:
        answ=True
    return answ


def date(a:int, b:int, c:int):
    """
    This is calender check module
    Module check date if it is real return to us answer
    Return True or False
    :param init a,b,c:day,month,year
    :param bool asnw:
    :rtype: bool
    """
    try:
        a=int(a)
        b=int(b)
        c=int(c)
        if a<=31 and a>0 and c>0 or b==3 or b==5 or b==1 or b==7 or b==8 or b==10 or b==12:
            answ=True
        elif a>30 and a>0 and c>0 or b==4 or b==5 or b==9 or b==11:
            answ=False
        elif a<=30 and a>0 and c>0 or b==4 or b==5 or b==9 or b==11:
            answ=True
        elif c%4!=0 and b==2 and a==29 and c>0:
            answ=False
        elif help_date(a, b, c) and c>0:
            answ=True
    except:
        answ=print('Enter correct data')
    return answ

def special_key(a:str):
    """
    This is special key was made for XOR_cipher
    I did it, cuz' wanted to upgrade and make harder user's key
    With it you can use numbers, words, symbols in your key
    In proccess transform str to int
    Return int
    :param a str
    :param c int
    :rtype int
    """
    c=0
    for i in a:
        c+=ord(i)
        c1=int(c)
    return c1

def XOR_cipher(password:str, special_key:any):
    """
    Cipher, convert password(user's word) to unicode with ord and after ^ key, after this move conver to str by chr
    You can use it, without or with special_key, I done early, in practice_work.py I showed with special_key
    :param password str
    :param key any
    :param crypted str
    :rtype str
    """
    crypted=''
    for i in password:
        crypted+=chr(ord(i)^special_key)
    return crypted

def XOR_uncipcher(crypted:str, key:any):
    """
    Decrypter for XOR_cipher
    :param crypted str
    :param key any
    :rtype str
    """
    decrypted=XOR_cipher(crypted, key)
    return decrypted