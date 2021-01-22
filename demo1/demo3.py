"""
author:gcm
c_date:2021/1/22 10:21
u_date:2021/1/22 10:21
reversion:1.0
file_name:demo3
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
	name = "召唤师"
	sex = "男"
	return render_template("index.html", **locals())


if __name__ == '__main__':
	app.run(host="192.168.11.4", port="6786", debug=True)
