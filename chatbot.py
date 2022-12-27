
import telepot
from apscheduler.schedulers.blocking import BlockingScheduler
from telepot.loop import MessageLoop
import requests
import csv
import time

# Replace 123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ with your own token
# Get token by chatting with BotFather 
bot = telepot.Bot('123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ')

def handle(msg):
    print(msg)

MessageLoop(bot, handle).run_as_thread()

def job_function():
    now = time.strftime('%Y-%m-%d %H:%M:%S') 
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    price = r.text

    f = open('C:/Users/Viola/Documents/Computer networks/price.csv', 'a', newline="")
    fieldnames = ['Date', 'Price']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow({'Date': now, 'Price': price})
    f.close()

    # Replace 999999999 with your own id
    bot.sendMessage(999999999, price)

scheduler = BlockingScheduler()
job = scheduler.add_job(job_function,'cron', minute ='0-59')
scheduler.start()
