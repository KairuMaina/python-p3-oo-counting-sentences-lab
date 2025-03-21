#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Value must be a string")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Replace multiple sentence-ending punctuation with a period
        cleaned_value = re.sub(r'[.!?]+', '.', self._value)
        # Split on periods and filter out empty strings
        sentences = [s.strip() for s in cleaned_value.split('.') if s.strip()]
        return len(sentences)

# Example Usage
string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences())  # Output: 3
