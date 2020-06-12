# from sensor import temp, pres
from flask import Flask, render_template
from wtforms import Form, StringField, validators, PasswordField

app = Flask(__name__)

class RegistrationForm(Form):
    name = StringField('Name', [validators.length(min = 1, max = 50)])
    username = StringField('Username', [validators.length(min = 2, max = 30)])
    email = StringField('Email', [validators.Email])
    password = StringField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Passwords do not match!')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug = True)