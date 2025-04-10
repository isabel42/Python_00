import sys

argv = sys.argv

if len(argv) > 2:
    print("AssertionError: more than one argument provided")

elif len(argv) == 2:
    try:
        num = int(argv[1])
        if num % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
    except ValueError:
        print("AssertionError: argument is not an integer")
