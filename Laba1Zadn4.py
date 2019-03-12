
a = [int(input('Input number ' + str(i) + ': ')) for i in range(1, 11)]
print(a)

b = [x for x in a if x % 2 != 0] + [x for x in a if x % 2 == 0]
print(b)