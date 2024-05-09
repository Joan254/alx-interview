#!/usr/bin/python3
"""UTF-8 validation"""


def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer
    """
    num_bytes_to_follow = 0

    for byte in data:
        # Checking if it's the start of a character
        if num_bytes_to_follow == 0:
            # If the first bit is 0, it's a 1-byte character
            if byte >> 7 == 0b0:
                continue
            # If the first 2 bits are 110, it's a 2-byte character
            elif byte >> 5 == 0b110:
                num_bytes_to_follow = 1
            # If the first 3 bits are 1110, it's a 3-byte character
            elif byte >> 4 == 0b1110:
                num_bytes_to_follow = 2
            # If the first 4 bits are 11110, it's a 4-byte character
            elif byte >> 3 == 0b11110:
                num_bytes_to_follow = 3
            else:  # If it doesn't match any known pattern, it's invalid
                return False
        else:
            # If it's not the start of a character,
            # it should have the prefix 10
            if byte >> 6 != 0b10:
                return False
            # Decrease the number of bytes left to follow
            num_bytes_to_follow -= 1

    if num_bytes_to_follow != 0:
        return False

    return True
