from flask import Flask, request, session, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import pandas as pd
import graphs
import finnhub
import mysql.connector

app = Flask(__name__)

app.secret_key = 'margiegargie'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=20)
db = SQLAlchemy(app)
graph_color = '#F8F8F8'

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Party100",
  database='portfolio'
)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route('/', methods=['POST', 'GET'])
def portfolio():
    return render_template('portfolio.html')


@app.route('/stock', methods=['POST', 'GET'])
def homepage():
    finnhub_client = finnhub.Client(api_key='chk00cpr01qnu4tqu5r0chk00cpr01qnu4tqu5rg')
    stock = pd.DataFrame(finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249))
    stock_tbl = stock.to_html()
    return render_template('stock.html', line=graphs.line_graph(df=stock), tbl=stock_tbl)


@app.route('/report_bug', methods=['POST', 'GET'])
def reportBug():
    return render_template('report_bug.html')


@app.route('/c_v', methods=['POST', 'GET'])
def cV():
    return render_template('c_v.html')


@app.route('/notebook', methods=['POST', 'GET'])
def notebook():
    mycursor = mydb.cursor()

    mycursor.execute('SELECT * FROM notebooks')
    notebooks = pd.DataFrame(mycursor.fetchall(), columns=['id', 'name', 'file_location', 'last_updated'])

    return render_template('notebook.html', notebooks=notebooks, len=len(notebooks))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')