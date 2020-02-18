
# 장편영화를 이용하여, 고객 선호 장르를 파악하는 알고리즘 만들기
from pymongo import MongoClient
import random

client = MongoClient('localhost', 27017)
# short_movie_platform 이라는 DB를 가져오겠다.
db = client.Short_Movie_Platform
# all_long_movie 라는 변수에 DB값 담기
all_long_movie = list(db.Long_movie_1.find())
# all_main_genre 라는 변수에 main_genre DB값 담기(이것도 코드가 맞는지 모르겠오)
all_main_genre = list(db.Long_movie_1.find(['main_genre']))
# all_second_genre 라는 변수에 second_genre DB값 담기
all_second_genre = list(db.Long_movie_1.find(['second_genre']))


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
            comparison_movie_1_main_genre = comparison_movie_1['main_genre']
            #메인장르 배열을 돌리고,
            for movie_genre in all_main_genre:
                #선택한 영화 메인 장르 값과 메인장르 배열의 값이 같으면
                if comparison_movie_1_main_genre == all_main_genre[movie_genre]:
                    # 선택된 영화의 장르 값에 + 2 점(이거 코드가 맞는지 모르겠오)
                    genre_score[movie_genre].update(genre_score=+2)
            # 서브장르 배열을 돌리고,
            for movie_genre in all_second_genre:
                # 선택한 영화 서브 장르 값과 서브장르 배열의 값이 같으면
                if comparison_movie_1_main_genre == all_second_genre[movie_genre]:
                    # 선택된 영화의 장르 값에 + 1 점(이거 코드가 맞는지 모르겠오)
                    genre_score[movie_genre].update(genre_score=+1)

        # 만약 사용자가 comaprison_movie_2 을 고른다면,
        elif customer_choice == comparison_movie_2:
            comparison_movie_2_main_genre = comparison_movie_2['main_genre']
            for movie_genre in all_main_genre:
                if comparison_movie_2_main_genre == all_main_genre[movie_genre]:
                    genre_score[movie_genre].update(genre_score=+2)
            for movie_genre in all_second_genre:
                if comparison_movie_2_main_genre == all_second_genre[movie_genre]:
                    genre_score[movie_genre].update(genre_score=+1)


         print(genre_score)


