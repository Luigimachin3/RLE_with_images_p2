def to_rle_string(rle_data):
    res = ""
    for idx, num in enumerate(rle_data):
        if idx % 2 == 0:
            value = num
            res += str(value)
        elif idx % 2 != 0:
            if 10 <= num <= 15:
                res += chr(ord("a") + num - 10)
            else:
                value = num
                res += str(value)
            if idx < len(rle_data) - 1:
                res += ":"
    return res



