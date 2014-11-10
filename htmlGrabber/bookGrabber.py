from bs4 import BeautifulSoup

soup = BeautifulSoup(open("books.html"))

links = soup("div", {"class": "course_header"})

for link in links:
    print(link.h3.contents)

