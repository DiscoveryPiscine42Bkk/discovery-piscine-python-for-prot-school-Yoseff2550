first = int(input('Enter the first number: ')) 
second = int(input('Enter the second number: ')) 
answer = first * second 


print(f'{first} x {second} = {answer}')

if answer > 0:
    print('The result is positive.')
elif answer < 0:
    print('The result is negative.')
else:
    print('The result is positive and negative.') 