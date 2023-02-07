n = int(input('Введите количество кустов: '))
blueberry = [int(i) for i in input().split()]
max_value = 0
for i in range(n):
  if 0 < i & i < n-1:
    total_berries = blueberry[i] + blueberry[i-1] + blueberry[i+1]
    if total_berries >= max_value:
      max_value = total_berries
  elif i == 0:
    total_berries = blueberry[i] + blueberry[-1] + blueberry[i+1]
    if total_berries >= max_value:
      max_value = total_berries
  else:
    total_berries = blueberry[i] + blueberry[0] + blueberry[i-1]
    if total_berries >= max_value:
      max_value = total_berries   
print(max_value)