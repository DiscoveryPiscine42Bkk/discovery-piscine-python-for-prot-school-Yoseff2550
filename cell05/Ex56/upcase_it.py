import sys

if len(sys.argv) > 1:
    for arg in sys.argv[:]:
        print(arg.upper())
else:
    print('none')