import sys

if len(sys.argv) != 3:
    print('none')
else:
    keyword = sys.argv[1]
    string = sys.argv[2]
    

    count = string.count(keyword)

    if count > 0:
        print(count)
    else:
        print('none')