# 🔢 Number to Word Converter

A simple Python project that converts numbers into their English word representation.

Examples:

* `123` → `One Hundred Twenty Three`
* `2345` → `Two Thousand Three Hundred Forty Five`
* `1000000` → `One Million`

The project includes:

* A Python implementation using recursion
* Support for large numbers up to `10^15`
* A simple Streamlit web interface

---

## Features

* Convert integers into English words
* Supports numbers from `0` to `999,999,999,999,999`
* Recursive implementation
* Command-line version
* Streamlit web application

---

## Project Structure

```text
project/
│
├── CONSTANTS.py
├── number_to_word.py
├── app.py
└── README.md
```

### Files

#### `CONSTANTS.py`

Contains the constants used by the converter:

* Numbers below 20
* Tens (Twenty, Thirty, ...)
* Large number names (Hundred, Thousand, Million, Billion)

#### `number_to_word.py`

Contains the main conversion logic.

#### `app.py`

Streamlit user interface.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd number-to-word
```

Install dependencies (if you want to work with GUI):

```bash
pip install streamlit
```

---

## Running the CLI Version

```bash
python number_to_word.py
```

Example:

```text
Enter your number: 2345
Two Thousand Three Hundred Forty Five
```

---

## Running the Streamlit App

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal.

---

## Examples

| Input   | Output                                |
| ------- | ------------------------------------- |
| 0       | Zero                                  |
| 15      | Fifteen                               |
| 42      | Forty Two                             |
| 100     | One Hundred                           |
| 2345    | Two Thousand Three Hundred Forty Five |
| 1000000 | One Million                           |

---

## Concepts Practiced

This project is useful for learning:

* Python Functions
* Recursion
* Dictionaries and Lists
* Input Validation
* Modular Programming
* Streamlit Basics

---

## You can add

* Support negative numbers
* Support decimal numbers
* Add multiple languages
* Add copy-to-clipboard button
* Improve UI styling
* Add automated tests

