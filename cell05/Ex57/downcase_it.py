import sys

if len(sys.argv) > 1:
    for arg in sys.argv[:]:
        print(arg.lower(),end='')
else:
    print('none')