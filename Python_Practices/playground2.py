def swap_character(first, second):
    new_string = ""
    for i in first:
        if i == "c":
            new_string += second[2]
            break
        new_string += i
    new_string += ' '
    for y in second:
        if y == "z":
            new_string += first[2]
            break
        new_string += y
    return new_string

print(swap_character('abc','xyz'))