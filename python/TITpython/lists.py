#
list1=['World', 5, 'Friendship']
print(list1[0][0])
#
list1=['World', 5, 'Friendship',['World', 5, 'Friendship']]
print(list1[3][0][0])
#
list1=['World', 56, 'Friendship',['World', 5, 'Friendship']]
print(len(str(list1[1])))
#
list1=['World', 5, 6, -50, 10]
print(list1[0:2])
#
list1=['World', 5, 6, -50, 10]
print(list1[0::2])
#
list1=['World', 5, 6, -50, 10]
i=1
list1.insert(i, 'FLEX')
print(list1)
#
list1=['World', 5, 6, -50, 10]
i=1
list1.append('123')
print(list1)
#
list1=['World', 5, 6, -50, 10]
list2=[4, 5, 7, 10]
list1.extend(list2)
#
list1=['World', 5, 6, -50, 10]
list2=[4, 5, 7, 10]
list3=['Word', 'Excel', 'PP']
list3.sort(key=len, reverse=True)
list2.sort(key=int, reverse=True)
#
list1=['World', 5, 6, -50, 10]
list2=[4, 5, 7, 10]
list3=['Word', 'Excel', 'PP']
str1='I will be in field with horse'
print(str1.split(','))


print(type(list3))
print(type(''.join(list2)))
print(type(str(list1)))







