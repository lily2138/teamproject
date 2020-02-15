from selenium import webdriver
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.Long_Movie_Platform # 'Long_Movie_Platform' 이라는 이름의 db를 만듭니다.

driver = webdriver.Chrome('./chromedriver')
# 크롬 실행

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200213&tg=1'
# "장르 : 드라마" 로 정렬되어있는 url 링크 (장르마다 링크가 달라서 장르 변경시 링크 변경해야함)
driver.get(url)

driver.find_element_by_xpath("//*[@id='old_content']/table/tbody/tr[2]/td[2]/div/a").click()
# xpath 를 사용하여, 1위로 찍힌 영화명을 클릭 (클릭해야 영화정보가 있는 사이트로 넘어갈 수 있음)
soup = BeautifulSoup(driver.page_source, 'html.parser')


Long_movie_infos = soup.select('#content > div.article')
# 장르 '드라마' 에 있는 첫 번째 영화에서 추출해야하는 영화정보 제일 큰 셀렉터
Long_drama_movie_1_data = {
    'title': '',
    'poster': '',
    'director': '',
    'actor': '',
    'summary': '',
    'main_genre': ''
}
# 출력 양식 설정
for Long_movie_info in Long_movie_infos:
    title = '<영화제목>' + '\n' + str(
        Long_movie_info.select_one('div.mv_info_area > div.mv_info > h3 > a:nth-child(1)').text) + ' (' + str(
        Long_movie_info.select_one('div.mv_info_area > div.mv_info > strong').text) + ')'
    print(title + '\n')
    poster = '<영화포스터>' + '\n' + str(Long_movie_info.select_one('img').attrs['src']).replace('//', '')
    print(poster + '\n')
    director = '<감독>' + '\n' + str(
        Long_movie_info.select_one('div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a').text)
    print(director + '\n')
    actor = '<출연진>' + '\n' + str(
        Long_movie_info.select_one('div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p').text)
    print(actor + '\n')
    summary = '<줄거리>' + '\n' + str(Long_movie_info.select_one(
        'div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > h5').text) + '\n' + str(
        Long_movie_info.select_one(
            'div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p').text)
    print(summary + '\n')
    main_genre = '<장르>' + '\n' + str(Long_movie_info.select_one(
        'div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a').text)
    print(main_genre + '\n')

    Long_drama_movie_1_data = {
        'title': title,
        'poster': poster,
        'director': director,
        'actor': actor,
        'summary': summary,
        'main_genre': main_genre
    }
    # 하나의 딕셔너리로 변수를 만들어서, 효율적인 관리 추구
    db.Long_movie_1.insert_one(Long_drama_movie_1_data)
    # DB에 first_drama_movie_data 딕셔너리(바로 위에 있는)를 'Long_movie_1' 라는 목록이름으로 저장
driver.back()
# driver.close()