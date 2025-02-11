#membership 
my_tuple = (1,2,3)
print(2 in my_tuple)
print('a' in my_tuple)
# output - true, false

'''
# immutable
my_tuple = ('a', 'b', 'c')
my_tuple[0] = 'd'
# output - error

my_tuple = (9, 18, 17)
my_tuple[3] = 36
print (my_tuple) # output - TypeError: 'tuple' object does not support item assignment

new_tuple = my_tuple + (5, 10, 15)
print (new_tuple) 
'''

#Conversions
my_tuple = (9,8,7)
my_newlist = list(my_tuple)

my_list = [12, 13, 14]
my_tuple = tuple(my_list)

print (f"Converted list: {my_newlist}\n")
print (f"Converted tuple: {my_tuple}\n")


