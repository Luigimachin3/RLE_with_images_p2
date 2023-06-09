def to_hex_string(data):
    res = ""
    for item in data:
        if 10 <= item <= 15:
            res += chr(ord('a') + item - 10)
        else:
            res += str(item)

    return res


print(to_hex_string([3, 15, 6, 4]))
