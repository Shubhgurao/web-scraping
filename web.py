from bs4 import BeautifulSoup
with open("D:\web-scraping\index.html") as fp:
    soup = BeautifulSoup(fp)
soup = BeautifulSoup("<html>data</html>")
