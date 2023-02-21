def my_decorator(func):
    def wrapper():
        print("调用func之前.")
        func()
        print("调用func之后.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


say_whee()
