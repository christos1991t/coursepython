def state(temperature):

    if temperature <= 0:
        print('solid')
    elif temperature > 0 and temperature <= 100:
        print('liquid')
    elif temperature > 100:
        print('gas')
    return temperature
