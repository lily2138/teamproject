#from idlelib import window
#from datetime import datetime
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.Short_Movie_Platform  # 'dbsparta'라는 이름의 db를 만듭니다.

app = Flask(__name__)


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('study.html')


@app.route('/user', methods=['GET'])
def listing():
    result = list(db.Long_movie_1.find({}, {'_id': 0}))
    # articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result': 'success', 'Long_movie_1': result})


# API 역할을 하는 부분
@app.route('/user', methods=['POST'])
def saving():

    title = request.form['title']
    poster = request.form['poster']
    director = request.form['director']
    actor = request.form['actor']
    summary = request.form['summary']
    main_genre = request.form['main_genre']
    second_genre = request.form['second_genre']

    data = {
        'title': title,
        'poster': poster,
        'director': director,
        'actor': actor,
        'summary': summary,
        'main_genre': main_genre,
        'second_genre': second_genre,
    }

    db.ART.insert_one(data)
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)