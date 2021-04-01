import pandas as pd
import mysql.connector
import data_query
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('panel'))
    return render_template('login.html', error=error)


# Route for handling the panel page logic
@app.route('/panel', methods=['GET', 'POST'])
def panel():
    table_names = data_query.get_table()
    operators = ["=", "!=", ">", "<", ">=", "<="]

    col_names = data_query.get_all().columns

    return render_template("panel.html", table_names=table_names, col_names=col_names, operators=operators)







if __name__ == "__main__":
    app.run(debug=True)