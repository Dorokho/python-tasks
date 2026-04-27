def coincidence(lst=None, rng=None):
    if lst is None or rng is None:
        return[]
    
    result = []

    for num in lst:
        if isinstance(num, (int, float)):
            if rng.start <= num < rng.stop:
                result.append(num)

    return result

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
print(coincidence([10, 20, 30], range(0, 15)))