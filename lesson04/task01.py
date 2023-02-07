n = int(input('Введи значение N: '))
m = int(input('Введи значение M: '))
num_list1 = []
print('Введи поочередно все числа первого набора')
for i in range(n):
  num1 = int(input())
  num_list1.append(num1)
print(f'Первый набор чисел:{num_list1}')
num_list2 = []
print('Введи поочередно все числа первого набора')
for i in range(m):
  num2 = int(input())
  num_list2.append(num2)
print(f'Второй набор чисел:{num_list2}')
set_1 = set(num_list1)
set_2 = set(num_list2)
new_set = set_1.intersection(set_2)
print(sorted(new_set))