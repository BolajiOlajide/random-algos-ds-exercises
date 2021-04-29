def run_length_encoding(s):
    if s == "":
        return ""

    result = ""

    counter = 0
    last_char = None
    for char in s:
        if last_char is None:
            counter += 1
            last_char = char
            continue

        if char == last_char:
            counter+= 1
            continue

        result += f"{counter}{last_char}"
        last_char = char
        counter = 1

    result += f"{counter}{last_char}"
    return result

print(run_length_encoding("aaaaaa")) # 6a
print(run_length_encoding("")) # ""
print(run_length_encoding("abcd")) # 1a1b1c1d
print(run_length_encoding("aabcc")) # 2a1b2c
print(run_length_encoding("aabccaddddaa")) # 2a1b2c1a4d2a
