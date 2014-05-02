from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# Create the application
app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def home():
	return render_template('home.html')