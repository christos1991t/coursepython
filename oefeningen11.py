# oefening 1 2
def get_max():
    grades = [9.6, 9.2, 9.7]
    max_local = f'Max: {max(grades)}'
    min_local = f'Min: {min(grades)}'
    result = str(f'{max_local}, {min_local}')
    return result


max_global = get_max()
print(max_global)
