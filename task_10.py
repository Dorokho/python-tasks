def count_words(string):
    cleaned = ""    # записываю очищенный текст

    for char in string.lower():
        if char.isalnum():
            cleaned += char    # проверка буква или цифра
        else:
            cleaned += " "

    words = cleaned.split()    # разбиваем на слова

    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1    # подсчет слов

    return result

print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))