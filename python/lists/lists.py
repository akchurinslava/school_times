#####
name=input('What is your name?:')
words=list(name)

n=len(words)

print(f'{n} and {words}')
#####
name=input('What is your name?:')
words=list(name)

n=len(words)

print(f'{n} and {words}')
print('Remove')
t=input('What word need to be removed')
nt=words.count(t)
j=0
if nt==0:
    print(f'{t} not in list: {words}')
else:
    for i in range(len(words)):
        if words[i-j]==t:
            words.pop(i-j)
            j+=1
    print(f'Now {t} not in list, words in list:{words}')

    #####
    name=input('What is your name?:')
words=list(name)

n=len(words)

print(f'{n} and {words}')
print('Remove')
t=input('What word need to be removed:')
nt=words.count(t)
j=0
if nt==0:
    print(f'{t} not in list: {words}')
else:
    for i in range(len(words)):
        if words[i-j]==t:
            words.pop(i-j)
            j+=1
    print(f'Now {t} not in list, words in list:{words}')
t=input('What word need to find?:')
print(f'Word {t} on {words.index(t)} position')