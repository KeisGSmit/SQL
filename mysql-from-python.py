import os
import datetime
import pymysql
import json
from flask import Flask, render_template, flash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/<card_url>")
def about_card(card_url):
    card = {}
    with open("data/nvidia.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj['url'] == card_url:
                card = obj
    return render_template("card.html", card=card)


# Get username from Cloud9 workspace
# (Modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password="",
                            db='Chinook')


try:
    # run a Query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        list_of_names = ['Fred', 'fred']
        # prepare a string with the same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("Delete from Friends where NAME in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
