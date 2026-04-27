import string

def is_palindrome(s):
    s = str(s)
    cleaned = ''.join(cher.lower() for cher in s if cher.isalnum())

    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
print(is_palindrome("Hello!"))

