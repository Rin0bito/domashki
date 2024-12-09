def print_params(a=1, b='string', c=True):
    return a, b, c

x1 = print_params()
x2 = print_params(a=2, b=50)
print(x1)
print(x2)


values_list = ['Oleg', 26, True]
values_dict = {'a': 11, 'b': 'Vika', 'c': 15}


x3 = print_params(*values_list)
print(x3)
x4 = print_params(**values_dict)
print(x4)



values_list_2 = [15, 'Hi']
x5 = print_params(42, *values_list_2)
print(x5)