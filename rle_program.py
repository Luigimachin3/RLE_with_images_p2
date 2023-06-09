# Project 2: Part B - by Luis Martinez

from console_gfx import ConsoleGfx as gfx


# Prompt the user to enter the name of a file. The function corresponds to Option 1.
def load_file():
    filename = input("Enter name of file to load: ")
    return gfx.load_file(filename)


# Set image_data to be gfx.test_imag. The function corresponds to Option 2.
def load_test_image():
    image_data = gfx.test_image
    print("Test image data loaded.")
    return image_data


# Display the current image by calling ConsoleGfx.display_image(image_data). The function corresponds to Option 6.
def display_image(image_data):
    if image_data is None:
        print("Displaying image...\n(no data)")
    else:
        print('Displaying image...')
        gfx.display_image(image_data)


# Translates the data into a hexadecimal string (without delimiters).
def to_hex_string(data):
    res = ""
    for item in data:
        if 10 <= item <= 15:
            res += chr(ord('a') + item - 10)
        else:
            res += str(item)

    return res


# Returns the number of runs in the image data set.
def count_runs(flat_data):
    count = 1
    run = 1
    current = flat_data[0]
    for num in flat_data[1:]:
        if current == num:
            count += 1
            if count > 15:
                count = 1
                run += 1
        else:
            count = 1
            current = num
            run += 1
    return run


# Returns encoding (in RLE) of the raw data passed in.
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


# Returns decompressed size RLE data.
def get_decoded_length(rle_data):
    even_idx = 0
    for idx, num in enumerate(rle_data):
        if idx % 2 == 0:
            even_idx += num
    return even_idx


# Returns the decoded data set from the RLE encoded data.
def decode_rle(rle_data):
    res = []
    for idx in range(0, len(rle_data), 2):
        value = rle_data[idx + 1]
        repeated_times = rle_data[idx]
        res.extend([value] * repeated_times)
    return res


# Translates a string in hexadecimal format into byte data.
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


# Translates RLE data into human-readable representation.
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


# Translates a string in human-readable format into RLE byte data.
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


# Print RLE Menu
def rle_menu():
    print("\nRLE Menu\n"
          "--------\n"
          "0. Exit\n"
          "1. Load File\n"
          "2. Load Test Image\n"
          "3. Read RLE String\n"
          "4. Read RLE Hex String\n"
          "5. Read Data Hex String\n"
          "6. Display Image\n"
          "7. Display RLE String\n"
          "8. Display Hex RLE Data\n"
          "9. Display Hex Flat Data\n")


# This global variable is initialized to None, and it will be used to store the images data as a flat list of bytes.
flat_byte_data = None


# Display the Standalone Mode via the main() method, which includes the welcome message, the Test Rainbow, the RLE menu,
# and prompts the user for input.

def main():
    # Welcome Message
    print("Welcome to the RLE image encoder!\n")
    # Display the Spectrum Image or Color Test.
    print("Displaying Spectrum Image:")
    gfx.display_image(gfx.test_rainbow)
    print()

    while True:
        rle_menu()
        # Declare a global variable to store the image data.
        global flat_byte_data
        menu_option = input("Select a Menu Option: ")
        # Exit the program if the user enters option 0.
        if menu_option == "0":
            exit(0)
        elif menu_option == "1":
            # Load the image data from a file if the user chooses option 1.
            flat_byte_data = load_file()
        elif menu_option == "2":
            # Load the test image data if option 2 is selected.
            flat_byte_data = load_test_image()
        elif menu_option == "3":
            # Decode RLE data entered by the user and store the image data.
            rle_str = input("Enter an RLE string to be decoded: ")
            flat_byte_data = decode_rle(string_to_rle(rle_str))
            # Decode RLE data from a hex string entered by the user and store the image data.
        elif menu_option == "4":
            rle_hex_str = input("Enter the hex string holding RLE data: ")
            flat_byte_data = decode_rle(string_to_data(rle_hex_str))
            # Convert a hex string entered by the user to image data and store it.
        elif menu_option == "5":
            flat_str = input("Enter the hex string holding flat data: ")
            flat_byte_data = string_to_data(flat_str)
            # Display the image data.
        elif menu_option == "6":
            display_image(flat_byte_data)
            # If there is image data available, encode it as RLE data and display the resulting string.
        elif menu_option == "7":
            if flat_byte_data is None:
                print("RLE representation: (no data)")
            else:
                rle_rep = to_rle_string(encode_rle(flat_byte_data))
                print("RLE representation:", rle_rep)
                # Display the resulting hex string
        elif menu_option == "8":
            if flat_byte_data is None:
                print("RLE hex values: (no data)")
            else:
                rle_hex_rep = to_hex_string(encode_rle(flat_byte_data))
                print("RLE hex values:", rle_hex_rep)
                # Display its hex representation.
        elif menu_option == "9":
            if flat_byte_data is None:
                print("Flat hex values: (no data)")
            else:
                hex_rep = to_hex_string(flat_byte_data)
                print("Flat hex values:", hex_rep)
        else:
            # Display an error message if the user input is invalid.
            print("Error! Invalid input.")


if __name__ == "__main__":
    main()
