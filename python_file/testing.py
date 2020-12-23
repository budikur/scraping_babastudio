import requests
import bs4

data_courses=[]
print(data_courses)
url = 'https://academy.babastudio.com/course-package-frontend?page=6'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, features="html.parser")
courses = soup.find_all('div', class_='course__box')
i = 1
for course in courses:
    title = course.find('p', attrs={'class': 'title'}).text
    price = course.find('strong').text
    image = course.find('img', attrs={'class': 'img-responsive'})['src']
    info = course.find_all('p', class_='info__course')
    durasi = info[0].text
    durasi = durasi.replace('  Total Durasi Video Kursus ', '')
    murid = info[1].text
    materi = info[2].text
    struct_data = {
        'title course': title,
        'price': price,
        'image': image,
        'durasi': durasi,
        'jumlah murid': murid,
        'materi course': materi
    }
    data_courses.append(struct_data)
# print(data_courses)
if data_courses==[]:
    print('no more data')