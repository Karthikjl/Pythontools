import requests
from bs4 import BeautifulSoup
import smtplib



URL= 'https://www.amazon.in/dp/B08XVZRR21?pf_rd_r=Y8MHQEYDA02C8H7FHSVF&pf_rd_p=edbb8056-1e40-459f-8a08-23d964f4510c&pd_rd_r=0bf131ef-4297-40f1-b3b8-069976fec9e6&pd_rd_w=a37XP&pd_rd_wg=0j4cZ&ref_=pd_gw_unk'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id ="productTitle").get_text().strip()

    price = soup.find('span', class_='a-price-whole').get_text()
    price_without_comma = price.replace(',', '')  # remove the comma from the string
    price_without_period = price_without_comma.strip('.')  # remove the period from the string
    converted_price = float(price_without_period)

    if(converted_price > 1800):
        send_mail()
        print(title)
        print(converted_price)

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('kar333thic@gmail.com','rpdkxqkwxtcvydkk')

    subject = 'Price fell down'
    body = f'check the amazon link : {URL}'

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail('kar333thic@gmail.com','wicoso7552@wwgoc.com',msg)

    print("Message has been sended sucessfully")
    server.quit

check_price()