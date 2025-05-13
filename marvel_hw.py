from marvel import full_dict
from pprint import pprint

# Задание 2: Обработка ввода пользователя
def process_input():
    user_input = input("Введите id фильмов через пробел(например:3 8 15 23): ")
    parts = user_input.split()
    
    # Преобразуем элементы в int, заменяя нечисловые на None
    processed = map(lambda x: int(x) if x.isdigit() else None, parts)
    return list(processed)
