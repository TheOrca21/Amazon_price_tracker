import requests
from bs4 import BeautifulSoup
import smtplib
import os

header = {'Accept-Language': 'en-US', 'User-Agent': 'Mozilla'}
response = requests.get('https://www.amazon.in/Dell-Alienware-i9-12900H-39-62Cms-D569942WIN9/dp/B09TP13BDV/ref=sr_1_4?crid=1E4YFVWT35DYB&keywords=dell+alienware+laptop&qid=1702739709&sprefix=dell+a%2Caps%2C275&sr=8-4', headers=header).text
soup = BeautifulSoup(response, 'lxml')
price = soup.find(name='span', class_='a-price-whole').getText()
price = int(str(price).replace(',', '').replace('.', ''))
msg = f'Hey the Alien-ware price has dropped to {price}!'
if price < 330000:
    email = os.environ.get('email')
    password = os.environ.get('password')
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=f"Subject:Price drop!\n\n"
                                f"{msg}"
                            )
