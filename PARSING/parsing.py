import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

base = ""

def download(url):
    resp = requests.get(url, stream=True)
    r = open("/Users/egormacpro/Desktop/PARSING/images/" + url.split("/")[-1], "wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_url():
    for i in range(1, 8):
        url = "https://scrapingclub.com/exercise/list_basic/?page=" + str(i)  # Get link
        response = requests.get(url, headers=headers)  # Machine_link
        soup = BeautifulSoup(response.text, "html.parser")  # lxml
        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")  # find and print HTML
        for com in data:
            pag = ("https://scrapingclub.com/" + com.find("a").get("href"))  # make  page's link
            yield pag

def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")  # lxml
        card_body = soup.find("div", class_="card-body")
        image = "https://scrapingclub.com/" + soup.find("img", class_="card-img-top img-fluid").get("src")
        data = card_body.find("h3", class_="card-title").text
        price = card_body.find("h4").text
        card_text = card_body.find("p").text
        download(image)
        yield data, price, card_text, image, card_url

