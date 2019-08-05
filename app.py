from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# __name__ is just the name of the module


app.config['SECRET_KEY'] = '7418ca1ede9685bd3442b17d6b50a9af'

posts = [
    {
        'author': 'Amod Rai',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date_posted': 'August 4,2019'
    },
    {
        'author': 'Aman Rai',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date_posted': 'August 4,2019'
    }
]



@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)