def is_palindrome(text: str) -> bool:
  return text == text[::-1]

assert is_palindrome("сбербанк мод много денег") == False
assert is_palindrome("-HoHoHoHoH-") == True
assert is_palindrome("Pskov") == False
assert is_palindrome("/-_-/0о0~-&%_H012.3450543.210H_%&-~0о0/-_-/") == True
assert is_palindrome("") == True
