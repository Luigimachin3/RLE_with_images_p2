def encode_rle(flat_data):
    res = []
    count = 1
    current_num = flat_data[0]
    for num in flat_data[1:]:
        if current_num == num:
            count += 1
            if count >= 15:
                res.extend([count, current_num])
                count = 0
                current_num = num
        else:
            res.extend([count, current_num])
            count = 1
            current_num = num
    res.extend([count, current_num])
    return res


print(encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 3, 3, 3, 3]))
