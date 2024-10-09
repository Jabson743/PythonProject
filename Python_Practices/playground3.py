def remove_character(word):
    new_string = ""
    for character in word:
      if character not in word:
           new_string += character
    return new_string

print(remove_character("Hello"))

