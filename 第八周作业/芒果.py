x = int(input('想购买几个芒果：'))
a = int(x / 6)
b = x - a * 6
c = int(b / 4)
if b % 4 != 0:
    print('-1')
else:
    print(a + c)