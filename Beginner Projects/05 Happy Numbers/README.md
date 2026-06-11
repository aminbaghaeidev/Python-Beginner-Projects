# Happy Number Checker

A simple Python script that determines whether a given number is a **happy number**.

## What is a Happy Number?

A happy number is defined by the following process:

1. Take a positive integer and replace it with the **sum of the squares of its digits**.
2. Repeat the process until the number either reaches **1** (happy) or enters an **infinite loop** (unhappy).

**Example:**

```
19 → 1² + 9² = 82
   → 8² + 2² = 68
   → 6² + 8² = 100
   → 1² + 0² + 0² = 1 ✓ Happy!
```

## Getting Started


### Running the Script

```bash
python happy_number.py
```

You will be prompted to enter a number:

```
Enter your number: 19
19 is a happy number!
```

## How It Works

The `happy_number(number)` function uses a `set` to track previously seen numbers. If the process leads back to a number already in the set, it means the sequence is stuck in a cycle and the number is **not** happy. If the number reaches `1`, it is happy.

```python
def happy_number(number):
    seen_numbers = set()
    while number != 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = sum(int(i) ** 2 for i in str(number))
    return number == 1
```

## Example Output

| Input | Result    |
|-------|-----------|
| 19    | Happy     |
| 7     | Happy     |
| 4     | Not happy |
| 100   | Happy     |
