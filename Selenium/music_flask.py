import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.Long_Movie_Platform # 'Long_Movie_Platform' 이라는 이름의 db를 만듭니다.
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('movie_select.html')


@app.route('/post', methods=['GET'])
def listing():
    # 모든 document 찾기 & _id 값은 출력에서 제외하기
    result = list(db.movies.find({}, {'_id': 0}))
    # movies라는 키 값으로 영화정보 내려주기
    return jsonify({'result': 'success', 'movies': result})


## API 역할을 하는 부분
@app.route('/post', methods=['POST'])
def saving():
    # 클라이언트로부터 데이터를 받는 부분
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']


    # mongoDB에 넣는 부분
    movie = {'url': url_receive, 'comment': comment_receive, 'image': url_image,
               'title': url_title, 'desc': url_description}

    db.movies.insert_one(movie)

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=6600, debug=True)