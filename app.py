import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods = ['GET'])
def wave():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/count_vowels', methods = ['POST'])
def count_vowels():
    text = request.form['text']
    vowels = 0
    for i in text:
        if i in 'aeiou':
            vowels += 1
    return f'There are {vowels} vowels in "{text}"'

@app.route('/sort-names', methods = ['POST'])
def sort_names():
    names = request.form['names']
    split_text = names.split(',')
    split_text.sort()
    return ','.join(split_text)
    

@app.route('/add', methods = ['GET'])
def add():
    lst = ['Julia', 'Alice', 'Karim']
    new_names = request.args['name']
    new_names_split = new_names.split(',')
    lst.extend(new_names_split)
    lst.sort()
    return ', '.join(lst)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

