# Note: Decorator is a function that takes some func and adds some functionality to it.
def makePretty(func):
    def inner():
        print("I got innternally decorated.")
        return func()
    return inner()

@makePretty
def ordinary():
    print("I am just an ordinary person.")


# Note: When ordinary() is called, it actually calls the inner function inside makePretty.