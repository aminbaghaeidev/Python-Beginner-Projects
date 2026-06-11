# 🐍 Beginner Python Projects

A collection of 10 small Python projects built while learning the language — covering core concepts like OOP, recursion, probability, and web interfaces.

---

## 📁 Projects

| # | Project | Topics | Tools |
|---|---------|--------|-------|
| 01 | [Number Guesser](#01-number-guesser) | Loops, conditionals, random | Python |
| 02 | [Rock Paper Scissors](#02-rock-paper-scissors) | Game logic, user input | Python |
| 03 | [Happy Numbers](#03-happy-numbers) | Math, sets, while loops | Python |
| 04 | [Number Conversion](#04-number-conversion) | Binary, octal, hex, algorithms | Python |
| 05 | [Contact Book](#05-contact-book) | OOP, dictionaries, CLI | Python |
| 06 | [Password Generator](#06-password-generator) | OOP, ABC, secrets, cryptography | Python, Streamlit |
| 07 | [Monty Hall Problem](#07-monty-hall-problem) | Probability, simulation, statistics | Python, Streamlit |
| 08 | [Tic Tac Toe](#08-tic-tac-toe) | Game logic, 2D lists | Python |
| 09 | [Number To Words](#09-number-to-words) | Recursion | Python, Streamlit |
| 10 | [Website Availability Checker](#10-website-availability-checker) | HTTP requests, networking | Python |

---

## 🔍 Project Details

### 01 Number Guesser
The program picks a random number and the user tries to guess it. Gives higher/lower hints until the correct answer is found.

### 02 Rock Paper Scissors
A classic CLI game against the computer with randomized choices.

### 03 Happy Numbers
Determines whether a number is a **happy number** by repeatedly summing the squares of its digits until it reaches 1 (happy) or enters a cycle (unhappy).

> Example: `19 → 82 → 68 → 100 → 1 ✓`

### 04 Number Conversion
Converts numbers between **binary**, **octal**, **decimal**, and **hexadecimal** — implemented from scratch without Python's built-in conversion functions.

| Function | From | To |
|---|---|---|
| `decimal_to_binary` | Decimal | Binary |
| `decimal_to_octal` | Decimal | Octal |
| `decimal_to_hex` | Decimal | Hex |
| `octal_to_binary` | Octal | Binary |
| `hex_to_binary` | Hex | Binary |
| `binary_to_octal` | Binary | Octal |

### 05 Contact Book
A CLI contact manager that supports adding, editing, searching, viewing, and deleting contacts stored in memory.

### 06 Password Generator
Generates three types of passwords using Python's cryptographically secure `secrets` module:

- **Random** — configurable length, optional digits and symbols
- **Memorable** — random English words joined by a separator (powered by NLTK)
- **PIN** — numeric code of configurable length

Includes a **Streamlit** web interface.

### 07 Monty Hall Problem
Simulates the famous Monty Hall probability puzzle and demonstrates that **switching doors wins ~66% of the time** vs ~33% for staying.

Runs thousands of games and plots win rates in real time using a **Streamlit** live chart.

### 08 Tic Tac Toe
Two-player CLI Tic Tac Toe with win detection and board rendering.

### 09 Number To Words
Converts any number to its English word representation using **recursion**.

> Example: `1042` → `"one thousand and forty two"`

### 10 Website Availability Checker
Checks whether a list of URLs are online by sending HTTP requests and reporting their status.

---

## 🚀 Getting Started

### Clone the project

You have two ways for cloning all the projects in your computer

1. In github you can open the repo then click on the code button then click download zip finally you can extract the ZIP and open the folder in your IDE.

2. You can use git with this command and clone this repo in your computer!

```bash
git clone https://github.com/aminbaghaeidev/Python-Beginner-Projects.git
```

### Requirements

You can install each project requirements but if you want to install all the requirements you can do this instead:

1. open the project folder and run this

```bash
pip install -r requirements.txt
```

### Running a project

```bash
# CLI projects
python 01-Number-Guesser/src/main.py

# or
python 04-Contact-Book/main.py

# Streamlit projects
streamlit run 06-password-generator/app.py
streamlit run 07-monty-hall/app.py
```

## 🧑🏻‍💻Creator

[@aminbaghaeidev](https://github.com/aminbaghaeidev)
---


![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-natural--language-green)
