file = open('**.txt', 'r', encoding='utf-8')
line = file.read()
line1 = file.readline()
line2 = file.readlines()
print(line.replace('\n', ' '))
###
a=['1. fdsfdsf\n', '2. fdsnfiudsji\n', '3. ufjsdifjsd']
b=3
for i in a:
    i=i[b:]
    print(i)
###
for i in range(len(line2)):
    line2[i]=line2[i][b:].replace('\n','')
    print(line2)

file.close()

###
content_list = []
with open('**.txt', 'r', encoding='utf-8') as file:
    for content in file:
        #print(content, end='')
        #content_list.append(content.strip('\n'))
        content_list.append(content[content.find(' ') + 1:].strip('\n'))
print(content_list)

###
with open('**.txt', 'r', encoding='utf-8') as file:
    content_list2=[content[content.find(' ') + 1:].strip('\n') for content in file]
print(content_list2)

###
with open('1.txt', 'r', encoding='utf-8') as file, open('2.txt', 'w', encoding='utf-8') as file2:
    for content in file:
        file2.write(content[content.find(' ') + 1:]) #for list,tuple etc we need writelines