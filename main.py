import requests
from bs4 import BeautifulSoup
import smtplib
import os

header = {'Accept-Language': 'en-US', 'User-Agent': 'Mozilla'}
response = requests.get(URL, headers=header).text
soup = BeautifulSoup(response, 'lxml')
price = soup.find(name='span', class_='a-price-whole').getText()
price = int(str(price).replace(',', '').replace('.', ''))
msg = f'Hey price has dropped to {price}!'
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
