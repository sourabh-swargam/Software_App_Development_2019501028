from flask import Flask, render_template, request

app = Flask(__name__)
name_list = []
# app.static_folder = 'static'
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST","GET"])
def register():
	print('called')
	if request.method == "GET":
		return render_template("register.html")
	elif request.method == "POST":
		name_list.append(request.form.get("name"))
		name_list.sort()
		return render_template("user_list.html", names=name_list)
