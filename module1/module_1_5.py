immutable_var = 0, True, 'String'
print('Immutable tuple:', immutable_var)

immutable_var[0] = 1 #TypeError: 'tuple' object does not support item assignment

mutable_list = [0, True, 'String']
print('Mutable list:', mutable_list)

mutable_list[0] = 1
print('Mutable list:', mutable_list)

