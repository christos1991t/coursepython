# Oefening 1


while True:

    user_input = input('where are your from?: ')

    match user_input:
        case 'USA':
            print('Hello')
        case 'India':
            print('namaste')
        case 'Germany':
            print('hallo')
        case _:
            break


ingredients = ["john smith", "sen plakay", "dora ngacely"]

for i in ingredients:
    i = i.title()
    print(i)
