import os
import pymysql
import json
from flask import Flask, render_template, flash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Get username from Cloud9 workspace
# (Modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user = username,
                            password="",
                            db='Chinook')


try:
    # run a Query
    with connection.cursor() as cursor:
        sql = "Select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
