from module import *
from colorama import *
init()
print(Fore.GREEN)
print(Back.BLACK)


sportmen =[]
results = []


while True:
    a = input('0 - Exit\n1 - Show sportmen and results lists\n2 - Add sportmen\n3 - [N] best results\n4 - Sorted lists and results \
        \n5 - Top 3\n6 - Disqualification then entered salary\n7 - Find sportmen by name \
        \n8 - Save data to files\n:')
    if a == '0':
        print('The winners never quit and quiters never win')
        break
    elif a == '1':
        print(sportmen)
        print(results)
    elif a == '2':
        add_sportmen(sportmen, results)
    elif a == '3':
        n_results(sportmen, results)
    elif a == '4':
        sorted_lists(sportmen, results)
    elif a == '5':
        top3(sportmen)
    elif a == '6':
        disqualification(sportmen, results)
    elif a == '7':
        find_sportmen_by_name(sportmen, results)
    elif a == '8':
        save_data(sportmen, results)
    else:
        print('Something goes wrong, please try again')