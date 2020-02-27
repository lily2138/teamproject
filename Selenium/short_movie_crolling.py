from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.ART_Movie_Platform  # 'ART_Movie_Platform'라는 이름의 db를 만듭니다.

# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)
driver = webdriver.Chrome('./chromedriver')
# 단편영화 추출할  사이트로 들어간다.
url = 'http://www.kobis.or.kr/kobis/business/mast/mvie/findDiverMovList.do'
driver.get(url)

ART_Movie_ex = {
    'title': '',
    'poster': '',
    'director': '',
    'actor': '',
    'summary': '',
    'genre': ''
}

for i in range(10):

    driver.find_element_by_xpath("//*[@id='pagingForm']/div/ul/li[" + str(i + 1) + "]/a").click()

    for j in range(11):

        driver.find_element_by_xpath("//*[@id='listArea']/div/ul/li["
                                     + str(j + 1) +
                                     "]/div/strong/a").click()

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        Art_movie_infos = soup.select(
            'body > div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-draggable.ui-resizable')

        for Art_movie_info in Art_movie_infos:
            title = '<영화제목>' + '\n' + str(
                Art_movie_info.select_one(
                    'div.ui-dialog-titlebar.ui-corner-all.ui-widget-header.ui-helper-clearfix.ui-draggable-handle > div.hd_layer > div > strong').text)
            print(title + '\n')
            poster = '<영화포스터>' + '\n' + 'http://www.kobis.or.kr/' + str(
                Art_movie_info.select_one('img').attrs['src']).replace(
                '//', '')
            print(poster + '\n')
            # 감독 정보가 없을 경우를 위해서 if 구문 사용
            director_xpath = str(driver.find_element_by_class_name('staffMore').text)
            # if not a:  # true print('a is empty!') -> 빈 리스트 체크하기
            if not director_xpath:
                director = '<감독>' + '\n' + 'NONE'
                print(director + '\n')

            else:
                director_xpath_data = director_xpath.split('배우')[0].split('만든사람들')[1].split('감독')[1].replace('|', ',')
                director = '<감독>' + director_xpath_data
                print(director + '\n')
            # 배우 정보가 없을 경우를 위해서 if 구문 사용
            actor_xpath = str(driver.find_element_by_class_name('staffMore').text)
            # if not a:  # true print('a is empty!') -> 빈 리스트 체크하기
            if not actor_xpath or director_xpath:
                actor = '<배우>' + '\n' + 'NONE'
                print(actor + '\n')

            else:
                actor_xpath_data = str(
                    Art_movie_info.select_one('dl > div:nth-child(2) > dd > table > tbody > tr > td').text).split(']')[
                    1].strip().replace('|', ',')
                actor = '<배우>' + '\n' + actor_xpath_data
                print(actor + '\n')

            # if not a:  # true print('a is empty!') -> 빈 리스트 체크하기
            if not soup.find('p', class_='desc_info'):
                summary = '<줄거리>' + '\n' + 'NONE'
                print(summary + '\n')

            else:
                summary_xpath = str(soup.find('p', class_='desc_info').text).strip()
                summary = '<줄거리>' + '\n' + summary_xpath
                print(summary + '\n')

            genre_seletor = str(soup.find('dl', class_='ovf cont').text).split('|')[2]
            # print(genre_seletor)
            genre = '<장르>' + '\n' + genre_seletor.replace('\n', '').replace('\t', '').replace(' ', '')
            print(genre + '\n')

            ART_Movie_ex = {
                'title': title,
                'poster': poster,
                'director': director,
                'actor': actor,
                'summary': summary,
                'genre': genre
            }

            db.ART_movie_list.insert_one(ART_Movie_ex)

            driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/a[2]/span").click()