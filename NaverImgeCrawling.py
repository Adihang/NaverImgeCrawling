import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

print('--------네이버 이미지 검색결과 다운로드-------')

#검색 url만들기
baseurl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='
Search = input('네이버 이미지 검색어:')
baseurl += urllib.parse.quote_plus(Search)

#이미지 url 추출
html = urlopen(baseurl)
htmlcode = BeautifulSoup(html, "html.parser")
Searchnum = int(input('다운로드 받을 이미지 개수:'))
imghtml = htmlcode.find_all(class_='_img', limit = Searchnum)

#이미지 다운로드
num = 1
for i in imghtml:
    imgurl = i.attrs['data-source']
    with urlopen(imgurl) as img:
        with open(Search + str(num) + '.jpg', 'wb') as name:
            imghtml = img.read()
            name.write(imghtml)

    print(str(num)+'번째 이미지 다운로드 완료')
    num += 1
print('다운로드 완료')
