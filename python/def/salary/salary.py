#Module colorama must be installed, use -  pip3 install coloroma 
from salary_module import *
salary=[]
employee=[]
from colorama import *
init()
print(Fore.BLACK)
print(Back.CYAN)

while True:
    print('0 - Read from file\n1 - Add data\n2 - Save data\n3 - Delete employee \
    \n4 - Max salary\n5 - Min salary\n6 - Sorted salary and employees\n7 - Duplicated salary \
    \n8 - Find salary by employee\n9 - Less or greater then entered salary\n10 - Top 3 richest and poorest employees \
    \n11 - Average salary\n12 - Employee netto salary\n13 - Sort employees A to Z or Z to A \
    \n14 - Delete employees who have lower salary then average\n15 - Find employees who have greater then entered salary \
    \n16 - Exit')
    v=int(input('Please enter the number:'))
    if v == 1 :
        salary, employee = item_to_list(salary, employee)
        print(salary)
        print(employee)
    elif v == 2:
        item_to_list(salary, 'salary.txt')
        item_to_list(employee, 'employee.txt')
    elif v == 0:
        salary = r_from_file('salary.txt')
        print(salary)
        employee = name_from_file('employee.txt')
        print(employee)
    elif v == 3:
        salary, employee = delete(input('Name:'), salary, employee)
        print(salary)
        print(employee)
    elif v == 4 :
        maxsalary(salary, employee)
    elif v == 5:
        minsalary(salary, employee)
    elif v == 6:
        sorted_salary_names(salary, employee)
    elif v == 7:
        same_salary(salary, employee)
    elif v == 8:
        ac = input('Please enter name of worker:')
        find_salary_by_name(salary, employee, ac)
    elif v == 9:
        ac = int(input('Please enter salary:'))
        less_or_greater_salary(salary, employee, ac)
    elif v == 10:
        top_3(salary, employee)
    elif v == 11:
        average_salary(salary, employee)
    elif v == 12:
        netto_salary(salary, employee)
    elif v == 13:
        sorted_names(employee)
    elif v == 14:
        delete_lower_average_employees(salary, employee)
    elif v == 15:
        find_employees_greater_entered_salary(salary, employee)
    elif v == 16:
        print(Fore.BLACK, Back.GREEN + 'The winners never quit and quiters never win...')
        break
    else:
        print('Something goes wrong, please try again...')
