import requests
from bs4 import BeautifulSoup
import smtplib
import time
import os
from dotenv import load_dotenv
load_dotenv()

#can be any url 
URL = 'https://fieldcraftsurvival.com/mobility-gobag-black-gen-3/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}

def check_price():

  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')

  title = soup.find(itemprop="name").get_text()
  price = soup.find(attrs={"class": "price--withTax"}).get_text()
  converted_price = float(price[1:4])

  if converted_price < 140:
    send_mail()

  print(converted_price)
  print(title)

  if converted_price > 140:
    send_mail()



def send_mail(): 
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login(os.environ('GMAIL_ADDRESS'), os.getenv('GMAIL_PW') )

  subject = 'Price down!'
  body = 'Check the link: https://fieldcraftsurvival.com/mobility-gobag-black-gen-3/'

  msg = f"Subject: {subject}\n\n{body}"

  server.sendmail(
    'sulatrick19@gmail.com',
    'alvarado.danna@gmail.com',
    msg
  )

  print('Hey the message was sent')

  server.quit()


while(True): 
  check_price()
  time.sleep(43200)

