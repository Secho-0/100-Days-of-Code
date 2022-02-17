
def greet():
    print("Hello")
    print("Hows it goin?")
    print("Weathers wild eh?")


def greet_with_name(name):
    print(f"Hello {name}")


greet()
greet_with_name("Sarah")


def greet_w_keywords(name, loc):
    print(f"Hello {name}")
    print(f"Hows the weather in {loc}")

greet_w_keywords(loc = "here", name = "bob")
