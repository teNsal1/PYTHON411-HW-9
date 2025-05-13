from marvel import full_dict
from pprint import pprint

# Задание 2: Обработка ввода пользователя
def process_input():
    user_input = input("Введите id фильмов через пробел(например:3 8 15 23): ")
    parts = user_input.split()
    
    # Преобразуем элементы в int, заменяя нечисловые на None
    processed = map(lambda x: int(x) if x.isdigit() else None, parts)
    return list(processed)

# Задание 3: Фильтрация по id из ввода
def filter_by_ids(ids):
    valid_ids = {i for i in ids if i is not None and i in full_dict}
    return {k: v for k, v in full_dict.items() if k in valid_ids}

# Задание 4: Множество режиссёров
def get_unique_directors():
    return {movie['director'] for movie in full_dict.values() if movie.get('director')}

# Задание 5: Преобразование года в строку (опционально)
def year_to_string():
    return {k: {**v, 'year': str(v['year'])} for k, v in full_dict.items()}

# Задание 6: Фильмы на букву 'Ч'
def filter_by_letter():
    return dict(filter(lambda item: item[1]['title'] and item[1]['title'].startswith('Ч'), full_dict.items()))

# Задание 7: Сортировка по году
def sort_by_year():
    sorted_items = sorted(full_dict.items(), key=lambda x: x[1]['year'])
    return dict(sorted_items)

# Задание 8: Сортировка по году и названию
def sort_by_year_and_title():
    sorted_items = sorted(full_dict.items(), key=lambda x: (x[1]['year'], x[1]['title']))
    return dict(sorted_items)

# Задание 9: Однострочник (фильтр + сортировка)
one_liner = dict(sorted(filter(lambda x: x[1]['year'] > 2020, full_dict.items()), key=lambda x: x[1]['title']))

# Главная функция
def main():
    # Шаг 2
    ids = process_input()
    print("\nОбработанные ID:", ids)
    
    # Шаг 3
    filtered_dict = filter_by_ids(ids)
    pprint(filtered_dict, width=120, sort_dicts=False)
    print("\nЗадание 3 выполнено: Отфильтрованные фильмы по ID")
    
    # Шаг 4
    directors = get_unique_directors()
    pprint(directors, width=120)
    print("\nЗадание 4 выполнено: Уникальные режиссёры")
    
    # Шаг 5 (опционально)
    year_str_dict = year_to_string()
    pprint(year_str_dict, width=120)
    print("\nЗадание 5 выполнено (опционально): Года как строки")
    
    # Шаг 6
    ch_movies = filter_by_letter()
    pprint(ch_movies, width=120)
    print("\nЗадание 6 выполнено: Фильмы на букву 'Ч'")
    
    # Шаг 7
    sorted_by_year = sort_by_year()
    pprint(sorted_by_year, width=120)
    print("\nЗадание 7 выполнено: Сортировка по году")
    
    # Шаг 8
    sorted_by_year_title = sort_by_year_and_title()
    pprint(sorted_by_year_title, width=120)
    print("\nЗадание 8 выполнено: Сортировка по году и названию")
    
    # Шаг 9
    pprint(one_liner, width=120)
    print("\nЗадание 9 выполнено: Однострочник (фильмы после 2020, отсортированные по названию)")

if __name__ == "__main__":
    main()
