
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
        if n <= 1:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

r = Recursion()
print(r.fibonacci(4))
        



