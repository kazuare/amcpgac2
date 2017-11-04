"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
	
@app.route('/isPalindrome')
def isPalindrome():
    s = request.args.get('str', default = '*', type = str)
    return '1' if s == s[::-1] else '0'
