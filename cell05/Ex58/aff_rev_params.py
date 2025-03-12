import sys

if len(sys.argv) > 1:
    reversed_args = sys.argv[1:][::-1]
    for arg in reversed_args:
        print(arg)
else:
    print("none")