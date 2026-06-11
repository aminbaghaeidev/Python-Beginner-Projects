def decimal_to_binary(number: int) -> str:
    """Convert a decimal number to binary.

    :param number: A non-negative decimal integer
    :return: Binary representation as a string
    """
    if number == 0:
        return "0"

    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary


def decimal_to_octal(number: int) -> str:
    """Convert a decimal number to octal.

    :param number: A non-negative decimal integer
    :return: Octal representation as a string
    """
    if number == 0:
        return "0"

    octal = ""
    while number > 0:
        octal = str(number % 8) + octal
        number //= 8
    return octal


def decimal_to_hex(number: int) -> str:
    """Convert a decimal number to hexadecimal.

    :param number: A non-negative decimal integer
    :return: Uppercase hexadecimal representation as a string
    """
    if number == 0:
        return "0"

    digits = "0123456789ABCDEF"
    hexadecimal = ""

    while number > 0:
        remainder = number % 16
        hexadecimal = digits[remainder] + hexadecimal
        number //= 16

    return hexadecimal


def octal_to_binary(number: str) -> str:
    """Convert an octal number to binary.

    :param number: A non-negative octal integer (digits 0–7 only)
    :return: Binary representation as a string
    """
    if number == 0:
        return "0"

    number = str(number)

    otb = {
        '0': "000", '1': "001", '2': "010", '3': "011",
        '4': "100", '5': "101", '6': "110", '7': "111"
    }

    result = ''.join(otb[digit] for digit in number)

    return result.lstrip('0') or "0"


def hex_to_binary(number: int | str) -> str:
    """Convert a hexadecimal number to binary.

    :param number: A non-negative hexadecimal value (int or string, e.g. 'A3' or 163)
    :return: Binary representation as a string
    """
    if str(number) == "0":
        return "0"

    number = str(number).upper()

    htb = {
        '0': "0000", '1': "0001", '2': "0010", '3': "0011",
        '4': "0100", '5': "0101", '6': "0110", '7': "0111",
        '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
        'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
    }

    result = ''.join(htb[digit] for digit in number)

    return result.lstrip('0') or "0"


def binary_to_octal(number: str) -> str:
    """Convert a binary string to octal.

    :param number: A binary string consisting of '0' and '1' characters
    :return: Octal representation as a string
    """
    while len(number) % 3 != 0:
        number = '0' + number

    bto = {
        "000": '0', "001": '1', "010": '2', "011": '3',
        "100": '4', "101": '5', "110": '6', "111": '7'
    }

    octal = ""

    for i in range(0, len(number), 3):
        octal += bto[number[i:i+3]]

    return octal.lstrip('0') or "0"


if __name__ == '__main__':
    assert decimal_to_binary(45) == "101101"
    assert decimal_to_octal(45) == "55"
    assert decimal_to_hex(45) == "2D"
    assert hex_to_binary("2D") == "101101"
    assert binary_to_octal("101101") == "55"
    print("\nAll the test passed!")
