from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import jwt
import datetime
import hashlib

from api import login

app = Flask(__name__)

app.register_blueprint(login.bp)

from pymongo import MongoClient




@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"email": payload['email']})
        return render_template('index.html')

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login", msg="다시 로그인해주세요."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login", msg="로그인 정보가 존재하지 않습니다."))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)