# oefening 1 en 2 en 3
def age(year_of_birth, current_year=2023):
    age_user = current_year - year_of_birth
    return age_user


age_input = int(input("When were you born?"))

result = age(age_input)

if result >= 120:
    print('That is imposible')
else:
    print(f'Your are is {result}')

# oefening 4


def names():
    name_list = user_input.split(',')
    leng = len(name_list)
    return leng


user_input = input("Enter names seperate by commas:")
print(names())
