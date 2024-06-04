def is_palindrome(text):
    normalized_text = ''.join(filter(str.isalnum, text)).lower()
    return normalized_text == normalized_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")