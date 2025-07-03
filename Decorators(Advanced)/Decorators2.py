def smart_move(func):
    def inner(a, b):
        print(f"I am dividing {a} and {b}")
        if b == 0:
            print("Logical Error!")
            
        return func(a, b)
    return inner

@smart_move
def divide(a, b):
    print(a / b)

final = divide(25, 5)
print(final)

# Note: The decorator should call inner func not a func with arguments.