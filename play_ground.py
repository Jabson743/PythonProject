def custom(func):
    def wrapper(*args, **kwargs):
        print("************")
        print(func(*args, **kwargs))
        print("************")

    return wrapper


@custom
def display(name):
    return f" Welcome {name}"