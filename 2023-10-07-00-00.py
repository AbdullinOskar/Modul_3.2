def print_params(a = 1, b = 'Hello', c = True):
    print(a, b, c)

print_params(2,25, [1 , 2, 3])

values_list = 1, 'user', True

values_dict  = { 'a':1, 'b':'Hello', 'c':True}

print_params(*values_list)

print_params(**values_dict)

values_list_2 = 22, 'student'

print_params(*values_list_2, 42)