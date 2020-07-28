
# functions for sending emails

import yagmail
import web_scraper 
from database import Database
import os


class Emails:
    def __init__(self):
        pass


    def scrapeQuotes(self):
        """scrapes quotes then sends email"""
        quotes = web_scraper.scrape_quotes()
        with Database() as db:
            db.store_quotes(quotes)  # store quotes in database
            
        
    def send_email(self, quote, receiver):
        """ send quote as an email """
        yag = yagmail.SMTP("dailyquotesst@gmail.com", password=os.environ.get("EMAIL_PASS"))
        yag.send(to=receiver,subject="Here is your daily quote",contents=quote)


    def send_to_everyone(self):
        """send emails to everyone in user database"""    
        with Database() as db:
            selected_emails = db.select_emails() 
            quote = db.pick_random_quote()

            if not quote:
                self.scrapeQuotes()
                db.commit()
                quote = db.pick_random_quote()
            
            if selected_emails is not None:
                for receiver in selected_emails:
                    self.send_email(quote,receiver)   
            




