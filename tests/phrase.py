import pytest

def phrase(str):
    phrase = input("Set a phrase: ")
    assert len(phrase) <= 15

print(phrase(str))


