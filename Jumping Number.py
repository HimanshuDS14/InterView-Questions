n = int(input())

l = []
for i in range(n):
    if len(str(i)) == 1:
        l.append(i)
    if len(str(i))>1:
        t = str(i)
        if int(t[1]) - int(t[0]) == 1:
            l.append(int(t))
print(l)
