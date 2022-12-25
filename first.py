import requests 
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com.tr/Oyuncak-Mutfak-E%C4%9Fitici-Montessori-K%C4%B1rm%C4%B1z%C4%B1/dp/B0996BT8J6/ref=sr_1_39?keywords=%C3%A7ocuk+oyun+mutfa%C4%9F%C4%B1&qid=1668672813&qu=eyJxc2MiOiIwLjAwIiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=%C3%A7ocuk+oyun+mut%2Caps%2C154&sr=8-39'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find_all(id = "productTitle")  
    price = soup.find("span", {"class": "a-offscreen"}).get_text()
    
    return price




def send_mail(price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('furkanbalkaya346@gmail.com', 'lthxbvihbrxhoage')

    subject =f'FIYAT DUSTUUUU'
    body = f'price price price'
    
    msg = f"subject: {subject} body: {body} "
    print(msg)
    server.sendmail(
        'furkanbalkaya24@gmail.com',
        'furkanbalkaya346@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()


while(True):

    price = check_price()
    print(int(price[0:3]))
    if(int(price[0:3])<400):
        send_mail(price)
    time.sleep(60*360)




