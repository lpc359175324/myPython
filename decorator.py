# decorator专项练习
def log(paramete):
    def decorator_function(f):
        print("装饰器定制参数"+paramete)
        def decorator_function2(*args, **kwargs):

            return f(*args, **kwargs)
        return decorator_function2
    return decorator_function

@log("debug")
def demo():
    print("demo_function")

demo()