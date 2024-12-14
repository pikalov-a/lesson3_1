###  Рекурсия ##module_3_5
def get_multiplied_digits( number ):
    global result
    if len(str(number))>2:
#        print(str(number)[1:])
        result *= int(str(number)[0])
#        print('!!!',result)
        return get_multiplied_digits(int(str(number)[1:]))
    else:
#        print('последнее умножение вручную, последний вызов вызывал неустранимую ошибку ')
        result *= int(str(number))
        return result
last_number = 0
result = 1
get_multiplied_digits ( 40203 )
print('Результат итогового умножения ',result)
result = 1
get_multiplied_digits ( 2020202020202020202 )
print('Результат итогового умножения ',result)
result = 1
get_multiplied_digits ( 303030303 )
print('Результат итогового умножения ',result)
result = 1
get_multiplied_digits ( 5050505 )
print('Результат итогового умножения ',result)
