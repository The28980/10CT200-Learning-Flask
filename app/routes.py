from app import app
from flask import render_template

# Use command [python -m flask run] to run this code
# When changes to the code are made, save and refresh the instance before running

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Siggums'}
    return render_template('index.html', title='Home', user=user)