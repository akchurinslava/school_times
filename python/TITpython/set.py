my_tuple=(1, 2, 3, 4, 5, 6)
my_set={1, 2, 3, 4, 5, 6}
print(my_set == my_tuple) # False
print(my_set > my_tuple)# Error different data type
print(my_set == my_tuple) # True

my_tuple=(1, 2, 3, 4, 5, 6, 6, 4, 3)
my_set={1, 2, 3, 4, 5, 6}
print(set(my_tuple) == my_set)


my_str='Hello world'
my_str_set=set(my_str)
print(my_str_set)


my_tuple=(1, 2, 3, 4, 5, 6)
my_set={1, 2, 3, 4, 5, 6}
my_str='Hello world!'
my_str_set=set(my_str)
my_str2='Hello world slava!'
my_str_set2 = set(my_str2)

print(my_str_set | my_str_set2)
print(my_str_set & my_str_set2)