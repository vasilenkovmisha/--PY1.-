from random import sample
list_ = list(range(-10,11))
def get_unique_list_numbers() -> list[int]:
    return sample(list_, 15)  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
