"""
author:gcm
c_date:2021/1/23 11:28
u_date:2021/1/23 11:28
reversion:1.0
file_name:user
"""
from flask import request, render_template, session, redirect, url_for, flash,Blueprint
userbp = Blueprint("user",__name__)
users = [{
	"name": "gao",
	"email": "gao@qq.com",
	"password": "1",
}]


@userbp.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html", **locals())
	elif request.method == "POST":
		user = None
		email = request.form.get("email")
		password = request.form.get("password")
		for u in users:
			if u["email"] == email and u["password"] == password:
				session["user"] = email
				return redirect(url_for("main.index"))
		flash("用户名或密码错误")
		return redirect(url_for("user.login"))


@userbp.route("/logout")
def logout():
	session.pop("user")
	return redirect(url_for("main.index"))


@userbp.route("/regist", methods=["GET", "POST"])
def regist():
	if request.method == "GET":
		return render_template("regist.html", **locals())
	elif request.method == "POST":
		email = request.form.get("email")
		password = request.form.get("password")
		password2 = request.form.get("password2")
		for u in users:
			if u["email"] == email:
				flash("邮箱已经注册")
				return redirect(url_for('user.regist'))
		if password != password2:
			flash("密码不一致")
			return redirect(url_for('user.regist'))
		users.append({
			"name": email,
			"email": email,
			"password": password
		})
		return redirect(url_for('user.login'))
