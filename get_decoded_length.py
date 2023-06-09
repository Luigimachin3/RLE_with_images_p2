def get_decoded_length(rle_data):
    even_idx = 0
    for idx, num in enumerate(rle_data):
        if idx % 2 == 0:
            even_idx += num
    return even_idx


print(get_decoded_length([3, 15, 6, 4]))