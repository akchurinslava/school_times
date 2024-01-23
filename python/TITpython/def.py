def my_sum(c, d, my_list):
    s = c + d
    s = s + c
    s = s + d
    return s

a = int(input('a = '))
b = int(input('b = '))

my_list = [i for i in range(0, 60, 3)]
summa = my_sum(a, b, my_list)
print(summa)

###

def my_sum(c, d, my_list):
    s = c + d
    for index in range(len(my_list)):
        my_list[index] += s
    return s

a = int(input('a = '))
b = int(input('b = '))

my_list = [i for i in range(0, 60, 3)]
summa = my_sum(a, b, my_list)
print(summa)

####

nr1 = lambda x: 'Even number' if x % 2 == 0 else 'Odd number'
print(nr1(int(input('Enter number:'))))

if x := int(input('Number')) % 2 == 0:
    print('Even number')
else:
    print('Odd number')