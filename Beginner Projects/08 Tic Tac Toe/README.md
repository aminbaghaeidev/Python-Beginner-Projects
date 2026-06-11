# Tic Tac Toe

A simple command-line Tic Tac Toe game written in Python.

## Features

* Two-player game (`X` and `O`)
* Random selection of the starting player
* Input validation
* Prevents selecting an already occupied position
* Detects winners automatically
* Detects draw situations
* Clean object-oriented design using a Python class

## Game Board Positions

Players choose a number from **1** to **9** corresponding to the board positions below:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

## Requirements

* Python 3.6 or higher

## How to Run

1. Clone or download the project.
2. Open a terminal in the project directory.
3. Run:

```bash
python tic_tac_toe.py
```

## Example

```text
player X enter your choice (1-9): 5

[' ', ' ', ' ']
[' ', 'X', ' ']
[' ', ' ', ' ']

player O enter your choice (1-9): 1
```

## Project Structure

```text
tic_tac_toe.py
README.md
```

## Class Overview

### `TicTacToe`

Main class responsible for:

* Creating and managing the game board
* Handling player input
* Switching turns
* Checking for winners
* Detecting draw conditions
* Running the game loop

## Winning Conditions

A player wins when they occupy any of the following combinations:

* Horizontal rows
* Vertical columns
* Diagonals

Examples:

```text
1 2 3
4 5 6
7 8 9
```

Winning combinations:

* 1, 2, 3
* 4, 5, 6
* 7, 8, 9
* 1, 4, 7
* 2, 5, 8
* 3, 6, 9
* 1, 5, 9
* 3, 5, 7

