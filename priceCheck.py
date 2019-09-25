import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Casio-Vintage-Digital-Black-Watch/dp/B00HFPIIOI'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}

# Fetches the html content from the above URL and fetches the price using the price ID.
# Compares the price with the hardcoded threshold ( in this case 850 ) and if the price is below threshold, calls the send_email function.

def checkprice():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()

    print(title.strip())

    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:5])
    print(converted_price)

    if converted_price < 850:
        send_mail()
    else:
        print("The price has not gone below threshold")


# Function to send Email.

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('test.python.72@gmail.com', 'zklxtkpbbpqmjopn')

    subject = 'Price fell down!'

    body = 'Check the link: https://www.amazon.in/Casio-Vintage-Digital-Black-Watch/dp/B00HFPIIOI'

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'test.python.72@gmail.com',
        'tfftejas@gmail.com',
        message
    )

    print("THE EMAIL HAS BEEN SENT!")
    server.quit()


while(True):
    checkprice()
    time.sleep(3600)