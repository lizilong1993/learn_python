# yield : cache data
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b 
        a, b = b, a + b
        n = n + 1


for n in fab(5):
    print(n)
# another way
f = fab(5)
f.__next__()
f.__next__()
f.__next__()
f.__next__()
f.__next__()
f.__next__()