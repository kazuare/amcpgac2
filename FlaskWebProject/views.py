"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
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
    """Renders the home page."""
	k = 1
	try:
		k = request.args.get('string')
	except:
		k = "something exploded"
		
    return render_template(
        'index.html',
        title=k,
        year=datetime.now().year,
    )