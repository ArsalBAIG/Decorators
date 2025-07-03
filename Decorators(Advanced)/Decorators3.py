def smart_move(func):
    def inner(a, b):
        print(f"I am multiplying {a} and {b}")
        if b == 0:
            print("Logical Error!")
        return func(a, b)
    return inner

@smart_move
def multiply(a, b):
    print(a * b)

result = multiply(5, 5)
print(result)