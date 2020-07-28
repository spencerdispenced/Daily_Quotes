#!/usr/bin/env python3

# main file for web app

from flask import Flask, request, render_template

from database import Database



app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/thanks')
def thanks():
    return render_template('thank_you.html')

@app.route('/', methods=['POST'])
def my_form_post():
    email_address = request.form['email']
    with Database() as db:
        db.store_email(email_address)  # add email to database
    return thanks()


if __name__ == '__main__':
    app.run()    
    
 