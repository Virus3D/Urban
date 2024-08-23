my_dict = {'Ivan': 1984, 'Petr': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Ivan'))
print('Not existing value:', my_dict.get('Sergey'))
my_dict.update({'Fedor': 1976, 'Ira': 2000})
value = my_dict.pop('Petr')
print('Deleted value:', value)
print('Modified dictionary:', my_dict)
print('')

my_set = {1,1,5,6,False,True,'St',7,5,2,2,True}
print('Set:', my_set)
my_set.add(8)
my_set.add(76)
my_set.remove(2)
print('Modified set:', my_set)
