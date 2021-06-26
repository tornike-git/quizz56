# import requests
# from bs4 import BeautifulSoup
# import sqlite3
#
# conn = sqlite3.connect("my_database.sqlite")
# cursor = conn.cursor()
#
# cursor.execute('''
#                 CREATE TABLE if not exists tvshows
#                 (id integer primary key autoincrement,
#                 title varchar(150),
#                 year integer,
#                 rating float)
# ''')
#
# url = 'https://www.imdb.com/chart/tvmeter/'
# r = requests.get(url)
# # print(r.status_code)
# content = r.text
#
# soup = BeautifulSoup(content, 'html.parser')
# all_list = soup.find('tbody', class_='lister-list')
# tr = all_list.find_all('tr')
#
# for each in tr:
#     title_bar = each.find('td', class_='titleColumn')
#     title = title_bar.a.text
#     # print(title)
#
#     year_bar = each.find('span', class_='secondaryInfo')
#     year = year_bar.text
#     year = year.replace('(', '')
#     year = year.replace(')', '')
#     # print(year)
#
#     rating_bar = each.find('td', class_='ratingColumn')
#     rating = rating_bar.text.strip()
#     # print(rating)
#
#     cursor.execute("INSERT INTO tvshows (title, year, rating) values (?, ?, ?)",
#                    (title, year, rating))
#     conn.commit()
# conn.close()
