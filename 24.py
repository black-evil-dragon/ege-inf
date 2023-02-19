f = open('./24_demo.txt').read()
k = 1
m = 1


for i in range(0, len(f)):
    if f[i] == 'Y' and f[i + 1] == 'Y':
        k += 1
    else:
        m = max(m, k)
        k = 1

m = max(m, k)
print(m)
