# Fibonachi Zahlen durch Iteration Methode.

def fibonachi_zahlen(n):

    if n <= 0:
        return n
    a,b = 0,1

    fibsequence = []

    for i in range(n):
        fibsequence.append(a)

        a = b
        b = a+b
    return fibsequence


n = int(input("\n Gib eine Zahl um Fibunachizahl zu berechnen  ")) 

print(f"\n Die Fibonache Zahlen für {n} lauten {fibonachi_zahlen(n)}\n")
