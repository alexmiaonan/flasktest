"""
author:gcm
c_date:2021/1/22 9:35
u_date:2021/1/22 9:35
reversion:1.0
file_name:demo2
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
	return "欢迎加入德莱联盟！"


@app.route("/<int:pk>")
def detail(pk):
	return f"为了弗雷尔卓德！{pk}"


if __name__ == '__main__':
	app.run(host="192.168.11.4", port="6786", debug=True)
