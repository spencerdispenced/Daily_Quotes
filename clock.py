
# used for heroku scheduler

from emails import Emails


def daily_quotes():
    emails = Emails()
    emails.send_to_everyone()

if __name__ == '__main__':
    daily_quotes()