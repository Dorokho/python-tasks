def combine_anagrams(words_array):
    anagrams = {}

    for word in words_array:
        # приводим к нижнему регистру и сортируем буквы
        key = ''.join(sorted(word.lower())) 

        # добавляем слово в соответствующую группу
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)

    # возвращаем только группы
    return list(anagrams.values())

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar","creams", "scream"]))   
print(combine_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
