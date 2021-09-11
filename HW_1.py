# Python. HW_1
# 1) Создать переменную типа String
# 2) Создать переменную типа Integer
# 3) Создать переменную типа Float
# 4) Создать переменную типа Bytes
# 5) Создать переменную типа List
# 6) Создать переменную типа Tuple
# 7) Создать переменную типа Set
# 8. Создать переменную типа Frozen set
# 9) Создать переменную типа Dict
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
# 17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.

String = str('type String')
print('A variable of the String type =', String)

Integer = int(16)
print('A variable of the Integer type =', Integer)

Float = float(16)
print('A variable of the Float type =', Float)

a = 'bytes' .encode('utf-8')
Bytes = bytes(a)
print('A variable of the Bytes type =', Bytes)
a = b'\xd0\xb1\xd0\xb0\xd0\xb9\xd1\x82' .decode('utf-8')
print('A variable of the Bytes type =', a)

List = list([3, 7, 8, 2, 4])
print('A variable of the List type =', List)
List.remove(3)
print('The list after removing =', List)
List.sort()
print('Increasing order of the list =', List)

Tuple = tuple('Hello')
print('A variable of the Tuple type =', Tuple)

Set = set({'string', 'integer', 'float', 'bytes', 'string', 'integer'})
print('A variable of the Set type =', Set)

Fset = frozenset('string, integer, float, bytes, string, integer')
print('A variable of the FrozenSet type =', Fset)

Dict = {'Belarus': 'Minsk', 'Poland': 'Warsaw'}
print(Dict['Belarus']), print(type(Dict))

a = str('Hello')
b = str('World')
c = a+b
print(c)

a = int(9)
b = int(7)
c = a+b
print(c)

c = a/b
print(c)

c = a*b
print(c)

c = a//b
print(c)

c = a%b
print(c)

c =(7 + 12) ** 3 + 7 * 4 - 44 / 2**4
print(c)
