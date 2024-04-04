#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents
    a valid UTF-8 encoding
    """
    bytes = 0
    for num in data:
        byte = format(num, '#010b')[-8:]
        if bytes == 0:
            for bit in byte:
                if bit == '0':
                    break
                bytes += 1
            if bytes == 0:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if not (byte[0] == '1' and byte[1] == '0'):
                return False
        bytes -= 1
    return bytes == 0
