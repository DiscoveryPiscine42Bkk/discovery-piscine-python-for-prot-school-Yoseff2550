age = int(input('Please tell me your age: '))
print ('You are currently ' + str(age) + ' years old.')

years = 10

while years <= 30:
    future = age + years
    print(f'In {years} years, you\'ll be {future} years old.')
    years += 10