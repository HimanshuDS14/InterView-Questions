n = input()

l = []
for i in range(int(n)):

    if i <10:
        l.append(i)

    if i>=10:
        t = str(i)

        a = int(t[0])
        b = int(t[1])

        if (a-b == 1 or a-b == -1) or  (b-a == 1 or b-a ==-1):
            l.append(int(t))
print(l)        

