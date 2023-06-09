def string_to_rle(rle_string):
    res = []
    rle_string = rle_string.split(":")
    for item in rle_string:
        num = item[0:-1]
        hex_num = item[-1]
        res.extend([int(num)])
        if "a" <= hex_num <= "f":
            res.extend([ord(hex_num) - ord('a') + 10])
        else:
            res.extend([int(hex_num)])
    return res