
# manage database

import os
import psycopg2



DATABASE_URL = os.environ['DATABASE_URL']  

class Database:
    def __init__(self):
       self.connection = psycopg2.connect(DATABASE_URL, sslmode='require')  # used for deployed version
       self._cursor = self._connection.cursor()
       

    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self._connection.close()


    def closeDb(self):
        self.commit()
        self._connection.close()


    @property
    def connection(self):
        return self._connection


    @property
    def cursor(self):
        return self._cursor


    def commit(self):
        self.connection.commit()


    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())


    def fetchall(self):
        return self.cursor.fetchall()


    def fetchone(self):
        return self.cursor.fetchone()


    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


    def store_email(self, user_address):  # store email in database
        self.execute('''CREATE TABLE IF NOT EXISTS user_emails 
            (address TEXT NOT NULL UNIQUE)''')
        try:
            self.execute("INSERT INTO user_emails (address) VALUES (%s)", (user_address,))
        except psycopg2.Error as e:
            print("You already signed up!")
        
            
    def select_emails(self):  # select all emails from database
        self.execute('''CREATE TABLE IF NOT EXISTS user_emails 
                (address TEXT NOT NULL UNIQUE)''')
        self.execute("SELECT address FROM user_emails")
        address = self.fetchall()
        
        if address:
           return address
        else:
            return None


    def store_quotes(self, all_quotes):  # store quotes in DB
        self.execute('''CREATE TABLE IF NOT EXISTS quotes
            (body TEXT, author TEXT)''')
        self._cursor.executemany("INSERT INTO quotes(body,author) VALUES (%(body)s, %(author)s)", all_quotes)
        

    def pick_random_quote(self):  # select a random quote from DB
        try:
            self.execute("SELECT body,author FROM quotes ORDER BY RANDOM() LIMIT 1") # select a random quote
        except:
            return None
        quote = list(self.fetchall())
        
        if quote:
            return f"{quote[0][0]} \n\nby {quote[0][1]}"
        else:
            return None




