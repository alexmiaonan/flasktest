"""
author:gcm
c_date:2021/1/23 11:28
u_date:2021/1/23 11:28
reversion:1.0
file_name:main
"""
from flask import render_template,Blueprint
mainbp = Blueprint("main",__name__)
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

@mainbp.route("/")
def index():
	article = book["articles"]
	return render_template("index.html", **locals())


@mainbp.route("/<int:pk>")
def detail(pk):
	article = None
	for a in book["articles"]:
		if a["id"] == pk:
			article = a
	return render_template("detail.html", **locals())
