#
# Work in progress!
#

# Import Flask, the web application framework
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# Import the view functions, stored in views.py
import views

# Start the server
if __name__ == '__main__':
	views.app.run()