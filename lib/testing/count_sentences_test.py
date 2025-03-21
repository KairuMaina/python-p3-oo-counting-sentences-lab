import pytest
from count_sentences import MyString

def test_value_string():
    '''Raises ValueError if value is not a string.'''
    string = MyString()
    with pytest.raises(ValueError, match="Value must be a string"):
        string.value = 123
