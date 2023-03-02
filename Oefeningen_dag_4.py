# oefening 1
user_input = int(input('Dollar ammount:'))
ex_rate = 0.95
euros = user_input*ex_rate

print('How many dollars have you got?', user_input)
print('the ammount of euros is:')
print(euros)

# oefening 2 en 3
ranking = ['John', 'Sen', 'Lisa']

user_input_2 = int(input('Enter rank number'))
rank = user_input_2-1
print(ranking[rank])
user_input_3 = input('Name of athlete:')
rank_2 = ranking.index(user_input_3)+1
print(rank_2)
