import random

def isPalindrome(s):
    return s == s[::-1]

def getRandomFact():
    facts = [
             'Palindromes date back at least to 79 AD, as a palindrome was found as a graffito at Herculaneum, a city buried by ash in that year.',
             'The palindromic Latin riddle <<In girum imus nocte et consumimur igni>> (<<we go wandering at night and are consumed by fire>>) describes the behavior of moths.',
             'The most familiar palindromes in English are character-unit palindromes.',
             'Semordnilap (palindromes spelled backward) is a name coined for words that spell a different word in reverse.',
             'Some names are palindromes, such as the given names Hannah, Ada, Anna, Bob and Otto',
             'I dont actually care about palindromes'
             ]
    return random.choice(facts)
