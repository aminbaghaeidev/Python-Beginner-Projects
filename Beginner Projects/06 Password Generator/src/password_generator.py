"""
Main module for generating differentpasswords.
"""
import secrets
import string
import random
from abc import ABC, abstractmethod
from typing import List

import nltk


nltk.download('words')
class PasswordGenerator(ABC):
    """The main class of all the password generators
    """
    @abstractmethod
    def generate(self):
        """abstract method of all the generators
        """
        pass


class RandomPassword(PasswordGenerator):
    """Generates random password with all ascii characters and digits
    """
    def __init__(
            self,
            length: int = 8,
            include_digits: bool = False,
            include_symbols: bool = False
        ):
        self.password_chars: str = string.ascii_letters
        self.digits: str = string.digits
        self.symobls: str = string.punctuation
        self.length = length
        self.include_digits = include_digits
        self.include_symbols = include_symbols

    def generate(self) -> str:
        """Generates the password with random ascii chars.

        :return: password
        :rtype: str
        """
        if self.include_digits:
            self.password_chars += self.digits
        if self.include_symbols:
            self.password_chars += self.symobls
        password: str = ''
        for _ in range(self.length):
            random_char: str = secrets.choice(self.password_chars)
            password += random_char
        return password


class MemoryablePassword(PasswordGenerator):
    """Generates a memoryable password 
    """
    def __init__(
        self,
        separator: str = "-",
        number_of_words: int = 10,
        capitalization: bool = False
    ):
        self.vocabulary: List[str] = nltk.corpus.words.words()
        self.separator = separator
        self.capitalization = capitalization
        self.number_of_words = number_of_words

    def generate(self) -> str:
        """main function for generating a password.

        :return: Password
        :rtype: str
        """
        password_words = []
        if self.capitalization:
            for _ in range(self.number_of_words):
                if random.choice([True, False]):
                    password_words.append(secrets.choice(self.vocabulary).upper())
                else:
                    password_words.append(secrets.choice(self.vocabulary))
            # password_words = [secrets.choice(self.vocabulary).upper() for _ in range(self.number_of_words)]
        else:
            password_words = [secrets.choice(self.vocabulary) for _ in range(self.number_of_words)]
        mem_password = self.separator.join(password_words)
        return mem_password


class PinPassword(PasswordGenerator):
    """Generates a PIN password with random digits
    """
    def __init__(self, length: int = 4):
        self.digits: str = string.digits
        self.length = length

    def generate(self) -> str:
        """The main function for generating the PIN code

        :return: PIN code
        """
        pin: str = ''.join(secrets.choice(self.digits) for _ in range(self.length))
        return pin



def test_password(password_type: object):
    print(f"Testing {password_type.__class__.__name__}...")
    password = password_type.generate()
    if isinstance(password_type, RandomPassword):
        assert len(password) >= 8
        assert all(char in string.printable for char in password)
    if isinstance(password_type, MemoryablePassword):
        assert len(password) >= 10
    if isinstance(password_type, PinPassword):
        assert len(password) >= 4
        assert all(char in string.digits for char in password)
    return f"Here is your password: {password}"
    

def main():
    random_password = RandomPassword(include_digits=True, include_symbols=True, length=16)
    memoryable_password = MemoryablePassword(capitalization=True)
    pin_password = PinPassword()
    print(test_password(random_password))
    print(test_password(memoryable_password))
    print(test_password(pin_password))
    print("Done")


if __name__ == '__main__':
    main()
