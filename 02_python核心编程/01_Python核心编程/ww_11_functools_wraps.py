import functools

def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print("note something")
        return func()
    return wrapper

@note
def test():
    "test function"
    print("I am test")

if __name__ == '__main__':
    test()
    print(test.__doc__)