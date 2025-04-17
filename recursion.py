
class Recursion: 
    

    def iterative(n):
        for i in range(n):
            print(i+1)

    def recursive(self, n):
        if n > 10:
            print(f"done, n is {n}")
            return
        print(n)
        self.recursive(n+1)
        print("what is the value of n? ", n)
        return

    # Where recursion shines is when you use it to break down a problem into "subproblems", 
    # whose solutions can then be combined to solve the original problem.

    def fibonacci(self,n):
        if n <=1:
            return n
        print(f"n is {n}")
        a = self.fibonacci(n-1)
        print(f"n is {n}, a is {a}")
        b = self.fibonacci(n-2)
        print(f"n is {n}, b is {b}")
        return a + b

    def factorial(self, n):
        if n == 0:
            return 1
        a = self.factorial(n-1)
        print(f"n is {n}, a is {a}")
        prod = n * a
        return prod
    
r = Recursion()
#print(r.fibonacci(3))
print(r.factorial(2))       



