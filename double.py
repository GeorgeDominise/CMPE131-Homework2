<<<<<<< HEAD
def doubler(func):
    def math():
        func()
        func()
    return math

def solve():
    print("Hello, World")

solve = doubler(solve)
solve()
=======
def doubler(func):
    def math():
        func()
        func()
    return math

@doubler
def solve():
    print("Hello, world")
solve()
>>>>>>> cd6b13e59255ab58e7970fc7147543f56dd42268
