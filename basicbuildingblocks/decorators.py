import functools

# def my_decorator(func):
#     @functools.wraps(func)
#     def function_that_replace_func():
#         print("I am in he decorator")
#         func()
#         print("After the function runs")
#     return function_that_replace_func

# @my_decorator
# def my_function():
#     print("i am the function")

# my_function()


def decorators_with_argument(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_replaces_func(*args,**kwargs):
            print("i am in the decorator")
            if 57==number:
                print("not running the function")
            else:
                func(*args,**kwargs)
            print("going from decorator")
        return function_that_replaces_func
    return my_decorator

@decorators_with_argument(57)
def my_function2(num1,num2):
    print("i am the function", num1, num2)

my_function2(12,34)