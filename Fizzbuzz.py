# Fizzbuzz

def fizzbuzz(n):

    for i in range(1,n):

        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i %3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else: print(i)

n = int(input("Gib eine Zahl ein um Fizzbuzz zu spielen  "))
if n <=0:
    print("Gib eine Zahl, die größer Null ist! \n")
    n = int(input("Gib eine Zahl ein um Fizzbuzz zu spielen  "))

fizzbuzz(n)
