
def wrong(function):
    def wrapper(*args, **kwargs):
        print("This function is wrong")
        return function(*args, **kwargs)
    return wrapper