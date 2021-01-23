"""
author:gcm
c_date:2021/1/22 10:21
u_date:2021/1/22 10:21
reversion:1.0
file_name:demo3
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from views.user import userbp
from views.main import mainbp

app = Flask(__name__)
app.register_blueprint(userbp)
app.register_blueprint(mainbp)
app.secret_key = os.urandom(24)

if __name__ == '__main__':
	app.run(host="192.168.11.4", port="6786", debug=True)
