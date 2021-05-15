from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)

app.secret_key = "AKRAM IS HERE!"


class SecretForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[
                            DataRequired(message="Please enter your email address"),
                            Email(message="Invalid Email"),
                            Length(min=8)])
    password = PasswordField(label='Password',
                             validators=[DataRequired(message="please insert your password")])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = SecretForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
