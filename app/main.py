import json

from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, request
from wtforms import StringField, validators
import validators as val
from config import Config
from scripts.unified_parse import get_statistics

app = Flask(__name__)
app.config.from_object(Config)

def url_validator(form, field):
    if val.url(form.url.data) is not True:
        raise validators.ValidationError('uncorrect url!')

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


@app.route('/api', methods=['post'])
def url():
    if request.method == 'POST':
        url =request.args.get('url')
        if url:
            try:
                if val.url(url) is True:
                    json_result = get_statistics(url)
                    return json.dumps(json_result, ensure_ascii=False)
                else:
                    return json.dumps({'uncorrect url!': 400})
            except Exception:
                return json.dumps({'Underfined error!': 400})
        else:
            return json.dumps({'Underfined usage!': 400})
