n = int(input)
royxat = list(map(int, input().split))
# max_value = max(royxat)
# print(max_value)
max_value = royxat[0]
for son in royxat:
    if son > max_value:
        max_value = son
    
print(max_value)