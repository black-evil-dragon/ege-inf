from config import name

f = open('C:/Users/'+ name + '/Downloads/24_5646.txt').read().strip()

# 43??78???34

while 'KK' in f:
    f = f.split('KK')

l = []
for i in range(len(f)):
    n = '0123456789'
    if len(f[i]) == 11:
        x = f[i]
        if x[0] + x[1] == '43' and x[4] + x[5] == '78' and x[9] + x[10] == '34':
            if x[2] in n and x[3] in n and x[6] in n and x[7] in n and x[8] in n:
                l.append(x)
s = 1
for i in max(l):
    if i in '13579':
        s *= int(i)
print(s)