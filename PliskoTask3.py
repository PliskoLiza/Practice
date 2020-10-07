time = float(input('Input the duration of the calls in minutes '))
if time < 0:
    print('Error:invalid time')
elif time <= 50:
    print('You wil pay 100 hryvnes')
elif time <= 100:
    print('You will pay 150 hryvnes')
elif time > 100:
    sum = (150 + (time - 100) * 2)
    print('You will pay ', sum,' hryvnes')