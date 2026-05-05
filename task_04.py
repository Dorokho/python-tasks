def sort_list(lst):
    if not lst:    # если список пустой
        return lst
    
    # Находим исходные min и max
    min_val = min(lst)
    max_val = max(lst)

    # Меняем местами
    for i in range(len(lst)):
        if lst[i] == min_val:
            lst[i] = max_val
        elif lst[i] == max_val:
            lst[i] = min_val

    # Добавляем одно минимальное значение (исходное!)
    lst.append(min_val)

    return lst

print(sort_list([]))
print(sort_list([2, 4, 6, 8])) 
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
print(sort_list([3, 1, 4, 1, 5, 1, 9]))