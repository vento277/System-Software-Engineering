size = 7
x = size
a = 1

for i in range(size):
    for j in range(x - 1):
        print("", end = "")
    
    for k in range(a):
        if (i % 2 == 0):
            if (k % 2 == 0):
                print('*', end = "")
            else:
                print('-', end = "")
        else:
            if (k % 2 == 1):
                print('*', end = "")
            else:
                print('-', end = "")
    print()
    x = x - 1
    a = a + 1