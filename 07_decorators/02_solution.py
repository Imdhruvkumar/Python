def debug(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(str(f"{k}={v}") for k, v in kwargs.items())
        print(f"{func.__name__} is args {args_value} and {kwargs_value}")
        return result
    return wrapper



    



@debug
def greet(name,greeting="hello"):
    print(f"{greeting},{name}")


greet("chai", greeting="hanji")