# Number Base Converter

A lightweight Python utility that converts numbers between **binary**, **octal**, **decimal**, and **hexadecimal** bases — implemented from scratch without using Python's built-in conversion functions.

## Features

| Function | From | To |
|---|---|---|
| `decimal_to_binary` | Decimal | Binary |
| `decimal_to_octal` | Decimal | Octal |
| `decimal_to_hex` | Decimal | Hexadecimal |
| `octal_to_binary` | Octal | Binary |
| `hex_to_binary` | Hexadecimal | Binary |
| `binary_to_octal` | Binary | Octal |

## Getting Started

### Running the Script

```bash
python converter.py
```

## Usage

Import the functions you need and call them directly:

```python
from converter import decimal_to_binary, hex_to_binary, binary_to_octal

decimal_to_binary(45)       # "101101"
decimal_to_octal(255)       # "377"
decimal_to_hex(255)         # "FF"
octal_to_binary(55)         # "101101"
hex_to_binary("FF")         # "11111111"
binary_to_octal("101101")   # "55"
```

## Function Reference

### `decimal_to_binary(number: int) -> str`
Converts a non-negative decimal integer to its binary string representation using repeated division by 2.

### `decimal_to_octal(number: int) -> str`
Converts a non-negative decimal integer to its octal string representation using repeated division by 8.

### `decimal_to_hex(number: int) -> str`
Converts a non-negative decimal integer to its uppercase hexadecimal string representation using repeated division by 16.

### `octal_to_binary(number: str) -> str`
Converts an octal integer to binary by mapping each octal digit to its 3-bit binary equivalent.

### `hex_to_binary(number: int | str) -> str`
Converts a hexadecimal value (int or string) to binary by mapping each hex digit to its 4-bit binary equivalent.

### `binary_to_octal(number: str) -> str`
Converts a binary string to octal by grouping bits into triplets from right to left and mapping each group to its octal digit.

## Limitations

- All functions handle **non-negative integers only** — negative numbers are not supported.
- `octal_to_binary` does not validate that the input contains only digits `0–7`.
- `hex_to_binary` does not validate that the input is a well-formed hex string.
