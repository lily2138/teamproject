
# 장편영화를 이용하여, 고객 선호 장르를 파악하는 알고리즘 만들기
from pymongo import MongoClient
import random

client = MongoClient('localhost', 27017)
# short_movie_platform 이라는 DB를 가져오겠다.
db = client.Short_Movie_Platform
# all_long_movie 라는 변수에 DB값 담기
all_long_movie = list(db.Long_movie_1.find())

# 장르마다 점수 값 배정
genre_score = {
    'drama_score': 0,
    'fantasy_score': 0,
    'fear_score': 0,
    'romance_score': 0,
    'adventure_score': 0,
    'thriller_score': 0,
    'noir_score': 0,
    'documentary_score': 0,
    'comedy_score': 0,
    'family_score': 0,
    'mystery_score': 0,
    'war_score': 0,
    'animation_score': 0,
    'crime_score': 0,
    'musical_score': 0,
    'SF_score': 0,
    'action_score': 0
}


# 선호장르 점수 계산 알고리즘
def prefer_algorithm():
    for i in range(20):
        # all_long_movie에서 랜덤으로 2개 값 출력 (20번 반복)
        comparison_movie = random.sample(all_long_movie, 2)
        # comparison_movie 의 리스트 첫 번째 값
        comparison_movie_1 = comparison_movie[0]
        # comparison_movie 의 리스트 두 번째 값
        comparison_movie_2 = comparison_movie[1]
        print("당신이 선호하는 영화를 골라주세요!")
        # 잘 입력되었는지 출력해보기
        print(comparison_movie)
        print(comparison_movie_1)
        print(comparison_movie_2)
        # 만약 사용자가 comaprison_movie_1 을 고른다면, (★) 고른 image 의 값을 'customer_choice' 대신에 넣어야함 (이 부분은 프론트엔드 할 때 수정해야함)
        if customer_choice == comparison_movie_1:
            # 비교군 1 영화의 메인장르 변수에 담기
            # 선택된 영화의 메인장르 값에 + 2 점
            comparison_movie_1_main_genre = comparison_movie_1['main_genre']
            if comparison_movie_1_main_genre == '<1장르>\n드라마':
                genre_score.update(drama_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n판타지':
                genre_score.update(fantasy_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n공포':
                genre_score.update(fear_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n멜로/로맨스':
                genre_score.update(romance_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n모험':
                genre_score.update(adventure_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n스릴러':
                genre_score.update(thiller_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n느와르':
                genre_score.update(noir_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n다큐멘터리':
                genre_score.update(documentary_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n코미디':
                genre_score.update(comedy_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n가족':
                genre_score.update(family_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n미스터리':
                genre_score.update(mystery_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n전쟁':
                genre_score.update(war_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n애니메이션':
                genre_score.update(animation_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n범죄':
                genre_score.update(crime_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n뮤지컬':
                genre_score.update(musical_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\nSF':
                genre_score.update(SF_score=+2)
            elif comparison_movie_1_main_genre == '<1장르>\n액션':
                genre_score.update(action=+2)

            # 비교군 1 영화의 서브장르 변수에 담기
            # 비교군 1 영화의 서브장르 값에 + 1점
            comparison_movie_1_second_genre = comparison_movie_1['second_genre']
            if comparison_movie_1_second_genre == '<2장르>\n드라마':
                genre_score.update(drama_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n판타지':
                genre_score.update(fantasy_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n공포':
                genre_score.update(fear_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n멜로/로맨스':
                genre_score.update(romance_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n모험':
                genre_score.update(adventure_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n스릴러':
                genre_score.update(thiller_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n느와르':
                genre_score.update(noir_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n다큐멘터리':
                genre_score.update(documentary_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n코미디':
                genre_score.update(comedy_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n가족':
                genre_score.update(family_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n미스터리':
                genre_score.update(mystery_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n전쟁':
                genre_score.update(war_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n애니메이션':
                genre_score.update(animation_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n범죄':
                genre_score.update(crime_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n뮤지컬':
                genre_score.update(musical_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\nSF':
                genre_score.update(SF_score=+1)
            elif comparison_movie_1_second_genre == '<2장르>\n액션':
                genre_score.update(action=+1)
            # 메인장르는 무조건 구분이 되지만, 서브장르는 구분이 안되고 'None'값으로 나오는 것이 있어서 else 를 사용해서 마무리
            else:
                continue

        # 만약 사용자가 comaprison_movie_2 을 고른다면, (★) 고른 image 의 값을 'customer_choice' 대신에 넣어야함
        elif customer_choice == comparison_movie_2:
            # 비교군 2 영화의 메인장르 변수에 담기
            # 선택된 영화의 메인장르 값에 + 2점
            comparison_movie_2_main_genre = comparison_movie_2['main_genre']
            if comparison_movie_2_main_genre == '<1장르>\n드라마':
                genre_score.update(drama_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n판타지':
                genre_score.update(fantasy_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n공포':
                genre_score.update(fear_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n멜로/로맨스':
                genre_score.update(romance_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n모험':
                genre_score.update(adventure_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n스릴러':
                genre_score.update(thiller_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n느와르':
                genre_score.update(noir_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n다큐멘터리':
                genre_score.update(documentary_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n코미디':
                genre_score.update(comedy_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n가족':
                genre_score.update(family_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n미스터리':
                genre_score.update(mystery_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n전쟁':
                genre_score.update(war_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n애니메이션':
                genre_score.update(animation_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n범죄':
                genre_score.update(crime_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n뮤지컬':
                genre_score.update(musical_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\nSF':
                genre_score.update(SF_score=+2)
            elif comparison_movie_2_main_genre == '<1장르>\n액션':
                genre_score.update(action=+2)

            # 비교군 2 영화의 서브장르 변수에 담기
            # 선택된 영화의 서브장르 값에 + 1점
            comparison_movie_2_second_genre = comparison_movie_2['second_genre']
            if comparison_movie_2_second_genre == '<2장르>\n드라마':
                genre_score.update(drama_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n판타지':
                genre_score.update(fantasy_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n공포':
                genre_score.update(fear_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n멜로/로맨스':
                genre_score.update(romance_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n모험':
                genre_score.update(adventure_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n스릴러':
                genre_score.update(thiller_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n느와르':
                genre_score.update(noir_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n다큐멘터리':
                genre_score.update(documentary_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n코미디':
                genre_score.update(comedy_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n가족':
                genre_score.update(family_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n미스터리':
                genre_score.update(mystery_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n전쟁':
                genre_score.update(war_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n애니메이션':
                genre_score.update(animation_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n범죄':
                genre_score.update(crime_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n뮤지컬':
                genre_score.update(musical_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\nSF':
                genre_score.update(SF_score=+1)
            elif comparison_movie_2_second_genre == '<2장르>\n액션':
                genre_score.update(action=+1)
            else:
                continue

            print(genre_score)


