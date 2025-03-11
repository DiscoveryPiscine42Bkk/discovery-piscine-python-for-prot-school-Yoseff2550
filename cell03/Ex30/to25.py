X = int(input('Enter a number less than 25: '))

if X > 25:
    print('Error')
else:
    while X <= 25:
        print(f'Inside the loop, my variable is {X}')
        X += 1  