a = input('Введите список a')
b = input('Введите список b')
ai = a.split(' ')
bi = b.split(' ')
ci = [ai,bi]
print(ci)
for i in range(len(ci)):
    ci[i] = len(ci[i])
print(ci)


