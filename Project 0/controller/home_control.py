from flask import render_template

def get_home_page():
    return render_template('landing.html')