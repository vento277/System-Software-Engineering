# Handle the except error gracefully. 
# However, this is very costly so only apply when it is certain that there will be cases where value error happens. 
try: 
    x = int(input("Enter an integer: "))
except:
    print("Wrong input")

try: 
    x = int(input("Enter an integer: "))
    print(1/x)
except ZeroDivisionError:
    print("x cannot be o")
except:
    print("Something is wrong with the input")


    