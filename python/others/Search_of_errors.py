while True:
    try:
        a=abs(int(input('Enter a number:')))
        break
    except ValueError:
        print('This is not integer')
if a==0:
    print('Nothing to do with number')
else:
    print('Many odds and even')
    print()
    c=b=a
    even=0
    odds=0
    while b>0:
        if b%2==0:
            even+=1
        else:
            odds+=1
        b//=10
    print('even:', even)
    print('even:', odds)
    print()
    print('Now we inverse number')
    print()
    while a>0:
        n=a%10
        a=a//10
        b=b*10
        b+=n
    print('Inversed number is:', b)
    print()
    print('Check hypothesis of Syracuse')
    print()
    if c%2==0:
        print(c, 'even number')
    else:
        print(c, 'odd number')
    while c!=1:
        if c%2==0:
            c=c/2
        else:
            c=(3*c+1)/2
        print(int(c), end=" ")
    print()
    print('Hypothesis is right')
