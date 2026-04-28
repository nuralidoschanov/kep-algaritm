n = int(input())
a = list(map(int, input().split()))
a.sort()
for son in a:
    print(son, end=" ")