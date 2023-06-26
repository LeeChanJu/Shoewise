import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote


def extract_title_and_link_from_blog_tab(keyword):
    # 검색어로 네이버 검색 페이지 가져오기
    url = urllib.request.urlopen("https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query=" + quote(keyword)+ "review")

    # HTML 파싱
    soup = BeautifulSoup(url, 'html.parser')

    # 타이틀과 링크 저장할 리스트 생성
    result = []

    # 네이버 Blog tab에서 제목과 링크 추출
    for part in soup.find_all('a', 'api_txt_lines total_tit _cross_trigger'):
        title = part.get_text()
        href = part['href']
        # 딕셔너리 형태로 글 제목과 링크 저장
        result.append({'title': title, 'link': href})

    return result
