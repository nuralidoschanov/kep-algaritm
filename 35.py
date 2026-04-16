a = int(input())
b = int(input())
min_value = min(a, b)
max_value = max(a, b)
s = 0
for i in range(min_value, max_value + 1):
  if i % 4 == 0:
      s = s + 1
print(s)