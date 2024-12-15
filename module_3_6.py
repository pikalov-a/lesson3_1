###  Дополнительное практическое задание по модулю ##module_3_6.py
##Подробнее о функциях
def calculate_structure_sum(data_structure):
    global result1
    if isinstance(data_structure, list) or isinstance(data_structure, tuple):
        for i in range(len(data_structure)):
            if isinstance(data_structure, str):
                result1 += len(data_structure)
                return +len(data_structure)
            elif isinstance(data_structure, int):
                result1 += data_structure
                return +data_structure
            else:
#                result1 += int(str(data_structure[0]))
                return calculate_structure_sum(data_structure[i])
#        return result
    elif isinstance(data_structure, dict):
        for key in data_structure:
            if isinstance(data_structure, str):
                result1 += len(data_structure)
                return +len(data_structure)
            elif isinstance(data_structure, int):
                result1 += data_structure
                return +data_structure
            else:
                result1 += int(str(data_structure)[0])
                return calculate_structure_sum(dict(data_structure[key]))
##    elif isinstance(data_structure, tuple):
    else:
        if isinstance(data_structure, str):
            result1 += len(data_structure)
            return +len(data_structure)
        elif isinstance(data_structure, int):
            result1 += data_structure
            return +data_structure
        else:
            print(type(data_structure),data_structure)
result1=0
print(result1)
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
print(result)
print(result1)
# print(type([1, 2, 3]))
# print(type({'a': 4, 'b': 5}))
# print(type((6, {'cube': 7, 'drum': 8})))
# print(type("ghjksf"))
# print(type(2))
