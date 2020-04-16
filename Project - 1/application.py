from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# db.init_app(app)
# db = SQLAlchemy()

class User(db.Model):
	__tablename__ = "users"
	# id = db.Column(db.Serial, primary_key=True)
	name = db.Column(db.String, primary_key=True, nullable=False)
	pw = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	timestamp = db.Column(db.Date, nullable=False)

if User.query.all() == []:
	db.drop_all()
	db.create_all()
	db.session.commit()

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST","GET"])
def register():
	print('called')
	if request.method == "GET":
		return render_template("register.html")
	elif request.method == "POST":
		n = request.form.get("name")
		pw = request.form.get("pw")
		timestamp = datetime.datetime.now()
		mail = request.form.get("email")
		try:
			user = User(name=n, timestamp=timestamp, email=mail, pw=pw)
			db.session.add(user)
		except:
			return render_template("error.html")
		db.session.commit()
		return render_template("success.html", name=user)

@app.route("/login", methods=["POST","GET"])
def login():
	print('here')
	if request.method == "GET":
		return render_template("login.html")
	elif request.method == "POST":
		n = request.form.get("name")
		pw = request.form.get("pw")
		user = User.query.filter_by(name=n).all()
		if len(user) == 0:
			return render_template("error.html")
		print("THIS IS IT",user[0].name)
		return render_template("success.html", name=user[0])

@app.route("/admin")
def admin():
	user_list = User.query.all()
	user_list.sort(key = lambda x: x.timestamp)
	return render_template("admin.html", name=user_list)