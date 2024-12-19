###  Дополнительное практическое задание по модулю ##module_3_5
##Подробнее о функциях
def calculate_structure_sum(data_structure):
    global result1
#    result1=0
    if isinstance(data_structure, list):   ###or isinstance(data_structure, tuple):
        result=calc_list(data_structure)
    elif isinstance(data_structure, dict):
        result=calc_dict(data_structure)
    elif isinstance(data_structure, tuple):
        result=calc_tuple(data_structure)
    elif isinstance(data_structure, set):
        result=calc_set(data_structure)
    else:
        result = calc_sum(data_structure)

def calc_list(data_structure):
    global result1
    for i in range(len(data_structure)):
#        print(type(data_structure), data_structure)
        result = calculate_structure_sum(data_structure[i])
#        print(type(data_structure[i]), data_structure[i])
    return result1

def calc_tuple(data_structure):
    global result1
    for i in range(len(data_structure)):
        result = calculate_structure_sum(data_structure[i])
    return result1

def calc_dict(data_structure):
    global result1
    for key in data_structure:
        result = calc_sum(key)
        result = calculate_structure_sum(data_structure[key])
    return result1
def calc_set(data_structure):
    global result1
    for s in data_structure:
        result = calculate_structure_sum(s)
    return result1

def calc_sum(data_):
    global result1
    if isinstance(data_, str):
        result1 += len(data_)
#        print(result1,data_)
        return result1+len(data_)
    elif isinstance(data_, int):
        result1 += data_
#        print(result1,data_)
        return result1+data_
    else:
        print('балбес',type(data_), data_)
#        result=calculate_structure_sum(data_structure)
result1=0
#print(result1)
# #
##Входные данные (применение функции):
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
#print(result)
print(result1)
