def r_from_file(file:str) -> list:
    """
    Module created for reading salaries from file and convert them to list
    :param file:str
    :rtype list
    """
    file = open ('salary.txt', 'r', encoding='utf-8-sig')

    list = []
    for row in file:
        list.append(row.strip())
    file.close()
    return list


def name_from_file(file:str) -> list:
    """
    Module created for reading employees from file and convert it to list
    :param file:str
    :rtype list
    """
    file = open ('employee.txt', 'r', encoding='utf-8-sig')
    list = []

    for row in file:
        list.append(row.strip())
    file.close()
    return list

def item_to_list(s:list, e:list):
    """
    Module created for adding and saving data to list
    :param s:list
    :param e:list
    :rtype list
    """
    n=int(input('How much employee:'))
    for i in range(n):
        names = input ('Name:')
        e.append(names)
        salary = input ('Salary:')
        s.append(salary)
    return s, e


def delete(name:str, s:list, e:list):
    """
    Module created for deleting data to list
    :param s:list
    :param e:list
    :rtype list
    """
    a = e.count(name)
    position = 0
    for i in range(a):
        index = e.index(name, position)
        position = index
        e.remove(name)
        s.pop(index)
    return s, e

def maxsalary(s:list, e:list):
    """
    Module created for finding max salary
    :param s:list
    :param e:list
    :rtype maxsalary:int
    :rtype names:str
    """
    s=list(map(int, s))
    max_salary = max(s)
    a=s.count(max_salary)
    position = 0
    print(f'max salary is {max_salary}\nNames are:')
    for i in range(a):
        ind = s.index(max_salary, position)
        names = e[ind]
        print(names)
        position=ind+1
    return max_salary, names

def minsalary (a:list, b:list):
    """
    Module created for finding min salary
    :param a:list
    :param b:list
    :rtype maxsalary:int
    :rtype names:str
    """
    a=list(map(int, a))
    min_salary = min(a)
    c = a.count(min_salary)
    position = 0
    print(f'Min salary is {min_salary}\nNames are:')
    for i in range(c):
        index = a.index(min_salary, position)
        names = b[index]
        print(names)
        position = index + 1
    return min_salary, names

def sorted_salary_names(a:list, b:list):
    """
    Module created for sorting salaries and name from A to Z
    :param a:list
    :param b:list
    :rtype a, b, a1, b1:list
    """
    a = sorted(list(map(int,a)))
    b = sorted(b)
    a1 = sorted(a, reverse=True)
    b1 = sorted(b, reverse=True)
    print(f'{a}\n{b}\n{a1}\n{b1}')
    return a, b, a1, b1

def same_salary(a:list, b:list):
    """
    Module created for finding employees with same salary
    :param a:list
    :param b:list
    :rtype c, c1:list
    """
    a=list(map(int, a))
    c = []
    c1 = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                c.append(a[i])
    for i in range(len(c)):
        for j in range(len(a)):
            if c[i] == a[j]:
                c1.append(b[j])
    print(f'Duplicated salary is: {c}\nWorkers were repeated it: {c1} ')
    return c, c1


def find_salary_by_name(a:list, b:list, ac:str):
    """
    Module created for finding employees with same salary
    :param ac:str
    :param b:list
    :param b:list
    :rtype abc:'NonType'
    """
    a=list(map(int, a))
    q = 0
    while True:
        try:
            i = b.index(ac, q)
            abc = print(a[i])
            q = i + 1
        except:
            break
    return abc


def less_or_greater_salary(a:list, b:list, ac:int):
    """
    Module created for finding employees who have lower or greater salary then entered
    :param a:list
    :param b:list
    :param ac:int
    :rtype c_lower, c_name_lower, c_name_greater, c_greater:list
    """
    a=list(map(int, a))
    c_name_greater = []
    c_name_lower = []
    c_greater = []
    c_lower = []
    qw = 0
    qwe = 0
    for i in range(len(a)):
        if ac > a[i]:
            c_greater.append(a[i])
            c_name_greater.append(b[i])
            print(f'{c_name_greater[qw]} has {c_greater[qw]}$')
            qw += 1
            i += 1
        elif ac < a[i]:
            c_lower.append(a[i])
            c_name_lower.append(b[i])
            print(f'{c_name_lower[qwe]} has {c_lower[qwe]}$')
            qwe += 1
            i += 1
    return c_lower, c_name_lower, c_name_greater, c_greater

def top_3(a:list, b:list):
    """
    Module created for finding top 3 richest and poorest employees
    :param a:list
    :param b:list
    :rtype ac, acb:list
    """
    a=list(map(int, a))
    a1 = a.copy()
    b1 = b.copy()

    ac = []
    acb =[]

    for i in range(0, 3):   
        c = a.index(max(a))
        c1 = a1.index(min(a1))
        ac.append(b[c])
        acb.append(b1[c1])
        a.remove(max(a))
        a1.remove(min(a1))
        b.remove(b[c])
        b1.remove(b1[c1])
    print('The richest employees are:')
    for i in ac:
        print(i)
    print('The poorest employees are:')
    for i in acb:
        print(i)
    return ac, acb

def average_salary(a:list, b:list):
    """
    Module created for finding average salary
    :param a:list
    :param b:list
    :rtype average:float
    """
    a=list(map(int, a))
    average = sum(a)/len(a)
    average = int(average)
    if average in a:
        c = a.index(average)
        print(f'Average salary is: {average}$\nThis salary get: {b[c]}')
    else:
        print(f'Average salary is: {average}$')
    return average


def netto_salary(a:list, b:list):
    """
    Module created for calculating netto salary of employee
    :param a:list
    :param b:list
    :rtype netto:float
    """
    a=list(map(int, a))
    c = input("Please enter  worker's name: ")
    if c in b:
        q = a[b.index(c)]
        if q <= 1000:
            netto = q - (q*0.2)
        elif q >= 1000 and q<=2500:
            netto = q - (q*0.25)
        elif q > 2500:
            netto = q - (q*0.3)
        print(f'Employee netto salary is: {netto}$')
    elif c not in b:
        print('No employee with this name')
    return netto

def sorted_names(b:list):
    """
    Module created for sorting employees from A to Z and reverse
    :param a:list
    :param b:list
    :rtype b1: list
    """
    c = input('How you want to sort:\n1 - A to Z\n2 - Z to A\n:')
    if c == '1':
        b1 = sorted(b, reverse=False)
        print(f'Sorted names are:\n{b1}')
    elif c == '2':
        b1 = sorted(b, reverse=True)
        print(f'Sorted names are:\n{b1}')
    return b1

def delete_lower_average_employees(a:list, b:list):
    """
    Module created for deleting employees(and their salary) who has lower then average salary
    :param a:list
    :param b:list
    :rtype a, b:list
    """
    a=list(map(int, a))

    averag = int(sum(a)/len(a))
    c = 0

    for i in range(len(a)):
        if a[c] < averag:
            a.pop(c)
            b.pop(c)
        elif a[c] > averag:
            c += 1
    print('Next employees had salary more then average salary:')
    ac = 0
    for i in b:
        print(f'{i} {a[ac]}$')
        ac += 1    
    return a, b

def find_employees_greater_entered_salary(a:list, b:list):
    """
    Module created for finding employees who have greater salary then entered
    :param a:list
    :param b:list
    :rtype a, b:list
    """
    a=list(map(int, a))

    c = int(input('Please enter salary:'))
    ac = 0
    for i in range(len(a)):
        if a[ac] < c :
            a.pop(ac)
            b.pop(ac)
        elif a[ac] > c :
            ac += 1

    print(f'Next employees had salary more then {c} salary:')
    acb = 0
    for i in b:
        print(f'{i} {a[acb]}$')
        acb += 1
    return a, b