import sys
import os

sys.path.append(os.path.abspath("FlaskWebProject"))
import commonCode

def test_palindrome():
    assert commonCode.isPalindrome("aabaa")

def test_not_a_palindrome():
    assert not commonCode.isPalindrome("aaba")

def test_random_fact():
    fact = commonCode.getRandomFact()
    assert type(fact) is str
    assert not fact == ''



