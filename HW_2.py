# # 1) Создать 2 переменных типа String с разными значениями
# # 2) Создать 4 переменных типа Integer с разными значениями
# # 3) Создать 3 переменных типа Float с разными значениями
# # 4) Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=. Результаты вывести в консоль.
# # 5) Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. Результаты вывести в консоль.
# # 6) Реализовать 10 вариантов сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями
# #    (and, or, not). Результаты вывести в консоль.
# # 7) Сделать скрипт используя функцию input().
# #     1.Функция должна на вход принимать целое число.
# #     2.Выводить должна "Вы ввели число = (введённое число) которое (меньше/больше/равно) 30"
# # 8) Сделать скрипт используя функцию input().
# #     1.Функция должна на вход принимать целое число.
# #     2.Внутри функции должно сгенерироваться рандомное целое число(import random)...(random.randint(1, 100))
# #     3.Выводить должна "Вы ввели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"
# # 9) Сделать скрипт используя функцию input().
# #     1.Функция должна на вход принимать целое число.
# #     2.Внутри функции должно сгенерироваться рандомное 2 целых числа(import random)...(random.randint(1, 100))
# #     3.Выводить должна "Вы ввели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно)
# #     сгенерированному числу"
# # В заданиях 7, 8, 9, сами выберите какие условные операторы и сравнения использовать.
#
# #4

a, b, c, d = map(int, input('Enter four integers ').split())
print(a > b,
      a < c,
      a >= d,
      a <= b,
      a != d,
      b > a,
      b != c,
      b < c,
      b >= d,
      c != d,
      c <= a,
      c >= a,
      d < a,
      d != b,
      d > b)


#5
a, b, c = map(float, input('Enter three numbers float type ').split())
print(a <= b,
      a != d,
      b > a,
      b != c,
      b < c,
      b >= d,
      c != d,
      c <= a,
      c >= a)
#6
a, b, c = map(int, input('Enter three integers ').split())
print(a < b and c > a,
      a > b or a > c,
      a != b and a != c,
      not b != c,
      not a >= b and b < c,
      a != b and c != a,
      a > b and c < a,
      not a > c or a > c,
      a != b and a != c,
      not b != c,
      not a >= b and b < c)
# 7
a = int(input('Enter an integer '))
b = 30
if a < b:
    print(f"You entered a number {a} that is less than 30")
elif a > b:
    print(f"You entered a number {a} that is greater than 30")
elif a == b:
    print(f"You entered a number {a} that equals 30")

# 8
import random
a = int(input('Enter an integer '))
b = (random.randint(1, 100))
if a < b:
    print(f"You entered a number {a} that is smaller than the generated number {b}")
elif a > b:
    print(f"You entered a number {a} that is greater than the generated number {b}")
elif a == b:
    print(f"You entered a number {a} that equals the generated number {b}")

#9

while True:
      import random
      a = int(input('Enter an integer '))
      b = (random.randint(1, 100))
      c = (random.randint(1, 100))
      if c < a > b:
            print(f"You entered a number {a} that is greater  {b} and greater {c}")
      elif c > a < b:
            print(f"You entered a number {a} that is smaller  {b} and smaller {c}")
      elif c == a == b:
            print(f"You entered a number {a} that equals  {b} and equals {c}")
      elif c == a > b:
            print(f"You entered a number {a} that is greater  {b} and equals {c}")
      elif c < a == b:
            print(f"You entered a number {a} that equals {b} and greater {c}")
      elif c < a < b:
            print(f"You entered a number {a} that is smaller {b} and greater {c}")
      elif c > a > b:
            print(f"You entered a number {a} that is greater {b} and smaller {c}")
      elif c == a < b:
            print(f"You entered a number {a} that is smaller {b} and equals {c}")
      elif c > a == b:
            print(f"You entered a number {a} that equals {b} and smaller {c}")
      continue
