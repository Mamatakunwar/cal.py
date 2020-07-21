start_over = 'true'
while start_over = 'true':
    principle = int(input('type starting amount'))
    addition = int(input('type annual addition'))
    rate = float(input('type interest rate'))
    time = int(input('enter number of years to invest'))
    real_rate = rate * 0.01
    i = 1

    print('total',principle * (1 + real_rate))

    while i < time:
        principle = (principle + addition) * (1 + real_rate)
        i = i + 1
        print('total', principle)

    redo_program = input('to restart type y or to quit type any key')
    if redo_program == 'y':
        start_over = 'true'
    else:
        start_over = 'null'