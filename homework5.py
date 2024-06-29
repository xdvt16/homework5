# 1.
immutable_var = (1, True, 'tuple', 5.0)
print(immutable_var)
# 2.
# immutable_var[0] = 2 - будет ошибка: TypeError: 'tuple' object does not support item assignment.
# Кортеж относится к неизменяемым типам данных,
# тем не менее внутри он может содержать изменяемые типы.
# 3.
mutable_list = [0, True, False, 'Apple', 3.14]
mutable_list[0:5] = 'Orange', 32, 'Pop', 'Pudge', None
print(mutable_list)