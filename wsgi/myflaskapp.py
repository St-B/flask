from flask import Flask
from flask import render_template
from flask import abort, redirect, url_for
from wtforms import StringField, SubmitField, IntegerField
from wtforms import validators
# DataRequired, NumberRange
# from flask.ext.wtf import Form as Form
from flask_wtf import Form

class NameForm(Form):
    description = StringField('Was?', validators=[validators.DataRequired(message='input muss sein')])
    qty = IntegerField('Wie viel?', [validators.NumberRange(min=0, max=10)])
    submit = SubmitField('anlegen')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(404)

@app.route('/hello/', methods=['GET', 'POST'])
@app.route('/hello/<description>', methods=['GET', 'POST'])
def hello(description=None):
    testform = NameForm()
    if testform.validate_on_submit():
        description = testform.description.data
        testform.description.data = ''
        testform.qty.data = 0
        return 'success'
    if not testform.validate_on_submit():
        description = 'ungueltig'

    testform.label = 'testy'
    return render_template('hello.html', name=description, form=testform)






if __name__ == "__main__":
    app.debug = True
    app.run()

