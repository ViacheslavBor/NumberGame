from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
import random 

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
	session['number'] = random.randrange(0, 101)
	guess = int(request.form['number'])
	if guess > session['number']:
		flash('Too high')
	elif guess < session['number']:
		flash('Too low')
	else:
		guess == session['number']
		flash('You are a winner')
	return redirect("/")

@app.route('/reset')
def reset():
	session['number'] == session.pop('number')
	return redirect('/')

app.run(debug=True)