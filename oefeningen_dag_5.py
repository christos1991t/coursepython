# oefening 1
filenames = ['document', 'report', 'presentation']

for i, j in enumerate(filenames):
    row = f'{i}-{j.capitalize()}.{"txt"}'
    print(row)


# oefening 2
ips = ['100.122.133.105', '100.122.133.111']

user_input = int(input('Enter index of IP:'))

print(ips[user_input-1])
