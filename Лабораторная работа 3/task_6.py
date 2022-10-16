list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

ind = 0
max_ = list_numbers[ind]

for pos, number in enumerate(list_numbers):
    if number > max_:
        max_ = number
        ind = pos




list_numbers[ind], list_numbers[-1] = list_numbers[-1], list_numbers[ind]

print(list_numbers)