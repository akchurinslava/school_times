a=abs(int(input('Enter a number:')))
if a!=0 and a!=int:
    odds=0
    even=0
    while a>0:
        if a%2==0:
            odds+=1
        else:
            even+=1
        a=a//10
elif a==0:
    print('Nothing to do with zero')
else:
    a==float
    print('This is not integer')
print('odds in number= '+str(odds))
print('even in number= '+str(even))
