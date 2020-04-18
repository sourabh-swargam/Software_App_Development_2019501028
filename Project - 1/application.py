from flask import Flask, render_template, request, session, url_for, redirect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def login_check(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'key' not in session :
            return redirect(url_for('auth'))
        return f(*args, **kwargs)
    return decorated_function

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

# db.drop_all()
# db.create_all()
# db.session.commit()

@app.route("/")
def index():
	if 'key' in session and 'user' in session:
		return render_template("user_home.html", name=session['user'])
	return render_template("index.html")

@app.route("/register", methods=["POST","GET"])
def register():
	if request.method == "GET":
		return render_template("register.html", flag = False)
	elif request.method == "POST":
		n = request.form.get("name")
		pw = generate_password_hash(request.form.get("pw")) 
		timestamp = datetime.datetime.now()
		mail = request.form.get("email")
		try:
			user = User(name=n, timestamp=timestamp, email=mail, pw=pw)
			db.session.add(user)
		except:
			return render_template("error.html", type="error")
		db.session.commit()
		return render_template("success.html", name=user)



@app.route("/auth", methods=["POST", "GET"])
def auth():
	if request.method == "GET":
		return render_template("login.html")
	elif request.method == "POST":
		n = request.form.get("name")
		pw = request.form.get("pw")
		user = User.query.filter_by(name=n).all()
		if len(user) == 0:
			return render_template("register.html", flag=True)
		user = user[0]
		if n == user.name and check_password_hash(user.pw, pw):
			session['key'] = True
			session['user'] = user.name
			return redirect(url_for("user_home"))
		else:
			return render_template("error.html", type="wrong pw")

@app.route("/user_home")
@login_check
def user_home():
	return render_template('user_home.html', name = session['user'])


@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for("index"))

@app.route("/admin")
def admin():
	user_list = User.query.all()
	user_list.sort(key = lambda x: x.timestamp)
	return render_template("admin.html", name=user_list)