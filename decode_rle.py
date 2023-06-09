def decode_rle(rle_data):
    res = []
    for idx in range(0, len(rle_data), 2):
        value = rle_data[idx + 1]
        repeated_times = rle_data[idx]
        res.extend([value] * repeated_times)
    return res


print(decode_rle([3, 15, 6, 4]))