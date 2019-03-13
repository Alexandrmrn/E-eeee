
a = [int(input('Input number ' + str(i) + ': ')) for i in range(1, 11)]
print(a)
c = [a[1] for i in range(1, 6)]
b = [x for x in a if x % 2 != 0] + с
print(b)
