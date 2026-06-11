from random import randint

def random_number(start, end):
    """Returns a random number between start and end."""

    return randint(start, end)

if __name__ == '__main__':
    assert random_number(1, 1000)
    print("The test has been passed!")