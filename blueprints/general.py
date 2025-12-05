from flask import Blueprint, render_template

# Create blueprint
general = Blueprint('general', __name__)

@general.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@general.route('/about_us')
def about_us():
    """About Us page route"""
    return render_template('about_us.html')

@general.route('/thank_you')
def thank_you():
    """Thank You page route"""
    return render_template('thank_you.html')