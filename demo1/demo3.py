"""
author:gcm
c_date:2021/1/22 10:21
u_date:2021/1/22 10:21
reversion:1.0
file_name:demo3
"""
from flask import Flask, render_template

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


@app.route("/")
def index():
	article = book["articles"]
	return render_template("index.html", **locals())


@app.route("/<int:pk>")
def detail(pk):
	article = None
	for a in book["articles"]:
		if a["id"] == pk:
			article = a
	return render_template("detail.html", **locals())


if __name__ == '__main__':
	app.run(host="192.168.11.4", port="6786", debug=True)
