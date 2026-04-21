def combine_anagrams(words_array):
    anagrams = {}

    for word in words_array:
        key = ''.join(sorted(word.lower())) 

        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)

    return list(anagrams.values())

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar","creams", "scream"]))   
print(combine_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
