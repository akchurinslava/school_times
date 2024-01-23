from datetime import *
from my_module import *
isik = input("Enter isikukood: ")
numbers = []
isikukoodid = []
if len(isik) == 11:
    try:
        isik_list=list(isik)
        if int(isik_list[0]) in [1,2,3,4,5,6]:
            if time(isik):
                print(check_of_summ(isik))
            else:
                print("Not correct month")
                numbers.append(isik)
                print(numbers)
        else:
            print("First number is wrong")
            numbers.append(isik)
            print(numbers)
    except:
        print("Incorrect data type, must be numbers")
        numbers.append(isik)
        print(numbers)
else:
    print("Symbols must be 11")
    numbers.append(isik)
    print(numbers)
