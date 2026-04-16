n = input().strip()
count = 0

for x in reversed(n):
    if x == '0':
        count += 1
    else:
         break

print(count)         
