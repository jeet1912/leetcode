def iterative(n):
    for i in range(n):
        print(i+1)

def recursive(n):
    if n > 10:
        print("done")
        return
    print(n)
    recursive(n+1)
    print("is it here")
    

#iterative(10)
recursive(1)