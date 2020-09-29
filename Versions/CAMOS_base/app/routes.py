from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Teacher'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'when ases tus momos en video-->'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'el futuro es hoy, oiste viejo :v'
		}
	]
	return render_template('index.html', title='Pagina principal', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, rebember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)

	
