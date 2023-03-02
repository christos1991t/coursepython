# oefening 1 en 2
while True:

    try:

        value_1 = int(input("Enter total value: "))
        value_2 = int(input("Enter value: "))

        perc = (value_2 / value_1)*100

        answer = f'That is {perc}'+'%'
        print(answer)

    except ValueError as ty:
        print('Please enter a number')
    except ZeroDivisionError as ze:
        print('Cannot divide with 0!')
