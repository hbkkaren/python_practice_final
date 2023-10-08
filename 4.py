a = [10,20,30,60,15]
b = [20,30,40,50]
c= []


for i in a:
    if i not in b:
        c.append(i)
for b in  b:
    c.append(b)

print(c)    