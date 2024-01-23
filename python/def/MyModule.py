def exit():
    """
    Module made for exit option in app, return exit phrase
    :param a str: pharase
    :rtype: str
    """
    a=print('The winners never quit and quiters never win \nGoodbye my FRIEND')
    return a

def FirstElif():
    """
    This module registration of users with own login and password
    :param l str:chosen login
    :param p str:chosen password
    :param log list:list of logins
    :param pasw list:list of passwords
    :rtype list
    """
    f = open('accounts.txt', 'a')
    l=input('Please enter your login: ')
    p=input('Please enter your password: ')
    f.write(f'\n{l}\n{p}\n')
    f.close()
    return f

def FirstElif2():
    """
    This module if users want to generate password by our system
    :param l str: user's login, user choices by itself
    :param p str: generated passwod
    :param words str: string which contain words for password generating
    :param log list: list of logins
    :param pasw list: list of passwords
    :rtype list
    """
    import random
    l=input('Please enter your login: ')
    p=''
    words = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(7):
        p+= random.choice(words)
    print('Your password will be:', p)
    f = open('accounts.txt', 'a')
    f.write(f'\n{l}\n{p}\n')
    f.close()
    return f

def SecondElif():
    """
    Module for authorization
    :param c str: user's login
    :param c1 str: user's password
    :param log list: list of logins
    :param pasw list: list of passwords
    :rtype list
    """
    while True:
        with open('accounts.txt', 'r') as file:
            line = file.read()
            c=input('Please enter your name: ')
            c1=input('Please enter your password: ')
            if c in line and c1 in line:
                print(f'Hello {c}!')
                break
        print('Invalid login or password!')
        break
    return line

def GrandElif():
    """
    In this module we concatenate a few modules to one
    :param b str: Choice of own password or generated
    :param log list: list of logins
    :param pasw list: list of passwords
    :rtype list
    """
    b=input('Do you want create your own password [yes, no]: ')
    if b.lower() == 'yes':
        FirstElif()
    elif b.lower() == 'no':
        FirstElif2()
    return FirstElif, FirstElif2

def GrandCrusade():
    """
    Grand module, here we concatenate all def functions together, just for save space
    :param a str: Choice of registration/authorization/exit
    :param log: list of logins
    :param pasw: list of passwords
    :rtype list
    """
    while True:
        a=input('What you want to do [registration, authorization, exit]: ')
        try:
            if a.lower() == 'exit':
                exit()
                break
            elif a.lower() == 'registration':
                GrandElif()
            elif a.lower() == 'authorization':
                SecondElif()
        except:
            print('Something goes wrong, please try again')
    return GrandElif, SecondElif






