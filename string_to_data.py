def string_to_data(data_string):
    res = []
    for char in data_string:
        if char.isdigit():
            res.extend([int(char)])
        elif "A" <= char <= "F":
            res.extend([ord(char) - ord('A') + 10])
        elif "a" <= char <= "f":
            res.extend([ord(char) - ord('a') + 10])
    return res


print(string_to_data("3f64"))