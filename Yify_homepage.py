from bs4 import BeautifulSoup
import requests

URL = "https://yts.am"
r = requests.get(URL).text
soup = BeautifulSoup(r, "lxml")
count = 1
for name in soup.find_all('div', class_="browse-movie-bottom"):
    movie_name1 = name.a.text
    if(count == 1):
        print("\n\n**************POPULAR DOWNLOADS**************\n\n")
    elif(count == 5):
        print("\n\n**************LATEST TORRENTS**************\n\n")
    elif(count == 13):
        print("\n\n**************UPCOMING YIFY MOVIES**************\n\n")
    print(movie_name1)
    count += 1
