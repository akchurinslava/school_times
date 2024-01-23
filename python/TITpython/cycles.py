n = input('Enter number: ')
while True:
    n -= 1
    if n<7:
        n+=4
    elif n>7:
        print(n)
    else:
        break
print('Hello world')


sum = 0
mult = 0
srzn=[0, 0]
for num in range(1, 101):
    if num%2 == 0 :
        sum += num
    else:
        mult *= num
    if num % 7 == 0:
        srzn[0] += num
        srzn[1] += 1
print('Summ of even number,', sum, '\nMultiple of odd numbers', mult)
print('Average of numbers multiples of seven', srzn[0], 'and  their quantity', srzn[1])


str1 = 'I like New Year'
for symb in str1:
    print(symb)


list1=[1,2,'r',7]
print(list[1])
list2=[i for i in range(1, 10) if i%2 == 0]
print(list2)