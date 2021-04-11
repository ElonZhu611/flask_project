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
    agg_funcs = ["COUNT", "DISTINCT", "MIN", "MAX", "AVG", ]

    if request.method == 'GET':
        col_names = data_query.get_all().columns
    else:
        table_name = request.form['table_name']
        col_names = data_query.get_1(table_name).columns

    return render_template("panel.html", table_names=table_names, col_names=col_names, 
                           operators=operators, agg_funcs=agg_funcs)





if __name__ == "__main__":
    app.run(debug=True)
