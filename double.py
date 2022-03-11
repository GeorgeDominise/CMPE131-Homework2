def doubler(func):
    def math():
        func()
        func()
    return math

def solve():
    print("Hello world.")

solve = doubler(solve)
solve()
