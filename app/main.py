from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template
from wtforms import StringField, validators
import validators as val
from config import Config
from scripts.unified_parse import get_statistics

app = Flask(__name__)
app.config.from_object(Config)

def url_validator(form, field):
    if val.url(form.url.data) is not True:
        raise validators.ValidationError('incorrect url!')

class Form(FlaskForm):
    url = StringField('url', validators=[DataRequired(), url_validator])
    submit = SubmitField('Send')
    result = StringField('result')

###TODO check https query is validated
@app.route('/',  methods=['GET', 'POST'])
def login():
    form = Form()
    if form.validate_on_submit():
        try:
            json_result = get_statistics(form.url.data)
            form.result.default = json_result
        except:
            return render_template('index.html', title='Sign In', form=form), 500



    return render_template('index.html', title='Sign In', form=form)
