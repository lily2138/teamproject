from pymongo import MongoClient
import random

client = MongoClient('localhost', 27017)
db = client.Short_Movie_Platform

# all_short_movie 라는 변수에 DB값 담기(지금 단편영화 db가 없어서 장편영화 db로 함)
all_long_movie = list(db.Long_movie_1.find({}))
# all_customer 라는 변수에 DB값 담기

#고객선택 장르 임의 설정
customer_genre1 = '드라마'
customer_genre2 = '판타지'


for k in range(len(all_long_movie)):
        #단편영화 장르 값 입시로 저장해두기
        temp_genre = all_long_movie[k].get('main_genre').split('\n')[1]
        # print(all_long_movie[k].get('main_genre').split('\n')[1])
        #만약에 고객 메인 장르와 단편영화의 임시장르가 같으면,
        if customer_genre1 == temp_genre :
            #그 영화들을 하나의 리스트로 모아둔다.
            temp_main_genre_movie.append(all_long_movie[k])
        # 만약에 고객 서브 장르와 단편영화의 임시장르가 같으면,
        if customer_genre2 == temp_genre:
            temp_second_genre_movie.append(all_long_movie[k])
        else:
            continue


#고객이 선호하는 장르 영화 리스트
print(temp_main_genre_movie)
print(temp_second_genre_movie)
#그 리스트 중에 샘플뽑기/ 첫번째 선호장르 영화3개 두번째 선호장르 영화 3개
print("첫번째 선호하는 장르영화는", customer_genre1)
print(random.sample(temp_main_genre_movie, 3)[0])
print(random.sample(temp_main_genre_movie, 3)[1])
print(random.sample(temp_main_genre_movie, 3)[2])

print("두번째 선호하는 장르영화는", customer_genre2)
print(random.sample(temp_second_genre_movie, 3)[0])
print(random.sample(temp_second_genre_movie, 3)[1])
print(random.sample(temp_second_genre_movie, 3)[2])


