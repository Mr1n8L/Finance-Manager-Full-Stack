from flask import render_template, redirect, url_for, request
from app import app, mongo

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    # Implement logic to retrieve and display user's income and total expense
    return render_template('dashboard.html')

@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # Implement logic to add new expense or monthly income to MongoDB
        return redirect(url_for('dashboard'))
    return render_template('add_transaction.html')

@app.route('/goal_setting')
def goal_setting():
    # Implement logic to retrieve and display user's goals
    return render_template('goal_setting.html')

