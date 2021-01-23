"""
author:gcm
c_date:2021/1/22 10:21
u_date:2021/1/22 10:21
reversion:1.0
file_name:demo3
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

book = {
	"name": "gcm",
	"author": "mm",
	"articles": [{
		"id": 1001,
		"title": "第一章",
		"content": "1111",
	}, {
		"id": 1002,
		"title": "第二章",
		"content": "2222",
	}, {
		"id": 1003,
		"title": "第三章",
		"content": "3333",
	},
	]
}
users = [{
	"name": "gao",
	"email": "gao@qq.com",
	"password": "1",
}]
currentuser = None


@app.route("/")
def index():
	global currentuser
	user = currentuser
	article = book["articles"]
	return render_template("index.html", **locals())


@app.route("/<int:pk>")
def detail(pk):
	global currentuser
	user = currentuser
	article = None
	for a in book["articles"]:
		if a["id"] == pk:
			article = a
	return render_template("detail.html", **locals())


@app.route("/login", methods=["GET", "POST"])
def login():
	global currentuser
	if request.method == "GET":
		return render_template("login.html", **locals())
	elif request.method == "POST":
		user = None
		email = request.form.get("email")
		password = request.form.get("password")
		for u in users:
			if u["email"] == email and u["password"] == password:
				currentuser = u
				return redirect(url_for("index"))
		return redirect(url_for("login"))


@app.route("/logout")
def logout():
	global currentuser
	currentuser = None
	user = currentuser
	return redirect(url_for("index"))


@app.route("/regist", methods=["GET", "POST"])
def regist():
	if request.method == "GET":
		return render_template("regist.html", **locals())
	elif request.method == "POST":
		email = request.form.get("email")
		password = request.form.get("password")
		password2 = request.form.get("password2")
		global users
		users.append({
			"name":email,
			"email": email,
			"password": password
		})
		return redirect(url_for('login'))


if __name__ == '__main__':
	app.run(host="192.168.11.4", port="6786", debug=True)
