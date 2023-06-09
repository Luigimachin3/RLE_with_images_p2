from rle_program import *

print(to_hex_string([3, 15, 6, 4]))  # opt 8 X

print(count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]))

print(encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]))  # X

print(get_decoded_length([3, 15, 6, 4]))

print(decode_rle([16, 2,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))  # calls encode_rle calls to_hex_string and to_rle_string (7 8 9)

print(string_to_data("3f64"))  # option 4 and option 5 call decode_rle

print(to_rle_string([3, 15, 6, 4]))   # X

print(string_to_rle("3f:64"))  # option 3 call decode_rle
