def doubler(func):
    def math():
        func()
        func()
    return math

def function():
    print("Hello world.")

function = doubler(function)
function()
