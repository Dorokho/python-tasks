def connect_dicts(dict1, dict2):
    # считаем суммы значений словарей
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    # определяем приоритетный словарь
    if sum1 > sum2:
        priority = dict1
        secondary = dict2
    else:
        priority = dict2
        secondary = dict1

    # объединяем словарь
    result = secondary.copy()
    result.update(priority)

    # удаляем элемент со значением меньше 10
    result = {k: v for k, v in result.items() if v >= 10}

    # сортируем по возрастанию
    result = dict(sorted(result.items(), key=lambda item: item[1]))

    return result

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))
print(connect_dicts({'a': 5, 'b': 15, 'c': 20}, {'b': 10, 'd': 25}))