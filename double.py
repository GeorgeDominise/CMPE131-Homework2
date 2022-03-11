def doubler(func):
    def math():
        func()
        func()
    return math

def solve():
    print("Hello, World")

solve = doubler(solve)
solve()
