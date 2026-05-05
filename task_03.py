def max_odd(array):
    max_value = None

    for x in array:
        # Проверяем, что это число
        if isinstance(x, (int, float)):

            # Если float, проверяем что он целый (например 21.0)
            if isinstance(x, float):
                if not x.is_integer():
                    continue
                x = int(x)

            # Проверяем нечётность
            if x % 2 != 0:
                if max_value is None or x > max_value:
                    max_value = x

    return max_value
            
print(max_odd(["a", 3, 5.0, 8]))                    
print(max_odd([1, 2, 3, 4, 4])) 
print(max_odd([21.0, 2, 3, 4, 4])) 
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) 
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))