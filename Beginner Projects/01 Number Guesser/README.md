# Number guesser project

<img src="https://www.funbrain.com/assets/img/content-cards/games%2Fguess_the_number.png" height=200px width=400px>

## Overview

This program provides a modular approach to the Number Guesser game with python. The game generates a random number between 1 and 100 then the user should import a number between this scope and the user will give a hint via score reducing if the user input wrong number. **If the user import wrong input the program will not crash.**

## Directory Structure
```
number guesser/
|-- src/
| |-- main.py
| |-- Logic
| | |-- comparison.py
| | |-- guess_number.py
| | |-- score.py
| |-- utils
| | |-- user_input.py
|-- README.md
|-- requirements.txt
```


## How to Run
1. Download the source from github
2. Download Python `3.13.5`
3. Open your terminal
4. Write the code below 
```bash
$ python src/main.py
```

## Modules
- `main.py`: The main program file that include all other modules and with running this you can see the game.
- `Logic`: Contains the core logic of the game.
  - `guess_number.py`: generate a random number.
  - `comparison.py`: compares the user input and computer guess.
  - `score.py`: calculates the score of the user.