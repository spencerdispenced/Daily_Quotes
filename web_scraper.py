
# functions for web scraping

import requests
from bs4 import BeautifulSoup
from time import sleep



def scrape_quotes():
    """ function to scrape all quotes from site """

    base_url = "https://www.goodreads.com/quotes"  # main url to scrape from
    url = "?page=1"  # url of page one

    all_quotes = []


    pages = 1
    while pages <= 100:
        res = requests.get(f"{base_url}{url}")  # # request this url
        soup = BeautifulSoup(res.text, "html.parser")  # send to BS to get parsed

        quotes = soup.find_all(class_="quoteDetails")  # find all classes called 'quoteDetails'

   
        for quote in quotes:  # pull the following from each quote
            body = quote.find(class_="quoteText").get_text(strip=True).split('\u2015',1)[0]
            author = quote.find(class_="authorOrTitle").get_text(strip=True).split(',',1)[0]

            all_quotes.append({"body" : body, "author" : author})
        
        sleep(2) 
        pages += 1
        url = f"?page={pages}"

    return all_quotes

