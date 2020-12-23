import requests
import bs4
import pandas as pd

data_courses = []
all_courses = []

def get_data(page):
    print('page: ',page)
    url = 'https://academy.babastudio.com/course-package-frontend?page='+ str(page)
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,features="html.parser")
    courses = soup.find_all('div',class_='course__box')
    i=1
    for course in courses:
        title = course.find('p',attrs={'class': 'title'}).text
        price = course.find('strong').text
        image = course.find('img',attrs={'class': 'img-responsive'})['src']
        info = course.find_all('p',class_='info__course')
        durasi = info[0].text
        durasi = durasi.replace('  Total Durasi Video Kursus ','')
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
        print(i,title)
        data_courses.append(struct_data)
        all_courses.append(struct_data)
        i+=1
    if data_courses==[]:
        print('no more data')
        return
    df = pd.DataFrame(data_courses)
    df.to_csv('/media/data/remoteworkerid/python/scraping_babastudio/csv_file/Data_course_page-'+ str(page) +'.csv',index=False,encoding='utf-8')

if __name__ == '__main__':
    page = 1
    get_data(page)
    while data_courses != []:
        page+=1
        data_courses.clear()
        get_data(page)
    df = pd.DataFrame(all_courses)
    df.to_csv('/media/data/remoteworkerid/python/scraping_babastudio/csv_file/Data_courses.csv',index=False, encoding='utf-8')
