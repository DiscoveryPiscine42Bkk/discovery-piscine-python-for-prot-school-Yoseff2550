import sys
if len(sys.argv) > 1:
    print("none")
    sys.exit(0)
num = 0 
while num <= 10:
    print(f"Table de {num}:", end=" ")
    i = 0 
    while i <= 10:
        print(num * i, end=" " if i < 10 else "\n")
        i += 1
    num += 1
