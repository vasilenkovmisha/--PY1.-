from random import sample
from string import ascii_letters, digits

all_symbols = ascii_letters + digits

def get_random_password(n=8) -> str:
    # TODO написать функцию генерации случайных паролей
    password = sample(all_symbols, n)
    text_password = ''.join(password)
    return text_password

print(get_random_password())