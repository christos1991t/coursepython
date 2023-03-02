def get_average():
    with open('data11.txt', 'r') as file_1:
        data = file_1.readlines()

    values = data[1:]
    values = [float(i) for i in values]
    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)
