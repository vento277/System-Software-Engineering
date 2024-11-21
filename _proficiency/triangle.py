def triangle(size):
    a = 1
    for i in range(size):
        lst = []
        b = a

        for j in range(size - (i+1)):
            lst.append(0)
        
        for g in range(i+1):
            lst.append(b)
            b -= 1   
                 
        for i in range(size):
            if lst[i] == 0:
                print(" ", end = "")
            else:
                print(lst[i], end = "")
        
        print()
        a += 1
        
triangle(7)
