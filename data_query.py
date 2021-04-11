import mysql.connector
import pandas as pd

def connect_info():
    host_ = "127.0.0.1"
    user_ = "root"
    password_ = "nbsbest"
    return host_, user_, password_

def get_table():
    mydb = mysql.connector.connect(
    	host = connect_info()[0],
    	user = connect_info()[1],
    	password = connect_info()[2]
    )
    mycursor = mydb.cursor(dictionary=True)
	# get all tables
    mycursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'new_schema'")
    tables = mycursor.fetchall()
    df_tables = pd.DataFrame(tables).TABLE_NAME
#    print(df_tables[0])
    return df_tables

def get_all():
	mydb = mysql.connector.connect(
		host = connect_info()[0],
		user = connect_info()[1],
		password = connect_info()[2]
	)
	mycursor = mydb.cursor(dictionary=True)
	# get all data
	mycursor.execute("SELECT * FROM new_schema.mock_data")
	data = mycursor.fetchall()
	df_all = pd.DataFrame(data)
	return df_all

def get_filters(filters_clause, filters_count, aggFunc, aggCol, start_date, end_date, groupCol):
    mydb = mysql.connector.connect(
		host = connect_info()[0],
		user = connect_info()[1],
		password = connect_info()[2]
        )
    mycursor = mydb.cursor(dictionary=True)

    if filters_count != 0:
        if (groupCol != "None") & (aggCol != "None") & (aggFunc != "None"):
            clause = "SELECT {}({}) FROM new_schema.mock_data WHERE {} AND date BETWEEN '{}' AND '{}' GROUP BY {}".format(filters_clause, aggFunc, aggCol, start_date, end_date, groupCol)
        else:
            clause = "SELECT * FROM new_schema.mock_data WHERE {} AND date BETWEEN '{}' AND '{}'".format(filters_clause, start_date, end_date)

    else:
        if (groupCol != "None") & (aggCol != "None") & (aggFunc != "None"):
            clause = "SELECT {}({}) FROM new_schema.mock_data WHERE date BETWEEN '{}' AND '{}' GROUP BY {}".format(aggFunc, aggCol, start_date, end_date, groupCol)
        else:
            clause = "SELECT * FROM new_schema.mock_data WHERE date BETWEEN '{}' AND '{}'".format(start_date, end_date)

    mycursor.execute(clause)
    data = mycursor.fetchall()

    df_final = pd.DataFrame(data).reset_index()

    return df_final



def get_columns(table_name):
    mydb = mysql.connector.connect(
    	host = connect_info()[0],
    	user = connect_info()[1],
    	password = connect_info()[2]
    )
    mycursor = mydb.cursor(dictionary=True)
    # get all data
    mycursor.execute(f"SELECT * FROM new_schema.{table_name}")
    data = mycursor.fetchall()
    cols = pd.DataFrame(data).columns
    # print(df_all)
    return cols
