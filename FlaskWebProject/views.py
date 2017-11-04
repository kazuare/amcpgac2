"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
import random
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='palindrome',
        year=datetime.now().year,
    )
	
@app.route('/isPalindrome')
def isPalindrome():
    s = request.args.get('str', default = '*', type = str)
    return '1' if s == s[::-1] else '0'

@app.route('/getRandomFact')
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