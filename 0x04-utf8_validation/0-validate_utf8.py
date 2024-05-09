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
    bytes_to_follow = 0

    for byte in data:
        binary = bin(byte).replace('0b', '').rjust(8, '0')[-8:]
        if bytes_to_follow == 0:
            if binary.startswith('110'):
                bytes_to_follow = 1
            if binary.startswith('1110'):
                bytes_to_follow = 2
            if binary.startswith('11110'):
                bytes_to_follow = 3
            if binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return False
            bytes_to_follow -= 1

    if bytes_to_follow != 0:
        return False

    return True
