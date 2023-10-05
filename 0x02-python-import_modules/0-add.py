#!/usr/bin/python3
if __name__ == "__main__":
    try:
        from add_0 import add
    except ImportError:
        print("Error: The 'add' function could not be imported.")
        exit(1)

    a = 1
    b = 2
    n = add(a, b)
    print("{} + {} = {}".format(a, b, n))
