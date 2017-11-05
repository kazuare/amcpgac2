"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
import commonCode
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def homeRequest():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='palindrome',
        year=datetime.now().year,
    )

@app.route('/isPalindrome')
def isPalindromeRequest():
    s = request.args.get('str', default = '*', type = str)
    return '1' if commonCode.isPalindrome(s) else '0'

@app.route('/getRandomFact')
def getRandomFactRequest():
    return commonCode.getRandomFact()