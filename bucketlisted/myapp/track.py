from myapp.models import *

from datetime import date
import time
from datetime import datetime
from email.message import EmailMessage
import ssl
import smtplib

from myapp.brain import *



def send_mail(sender, password, receiver, body, subject):
    em = EmailMessage()

    em['from'] = sender
    em['to'] = receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())

# traversing the model and checking if price has dropped :
# and emailing the user if price drops :

while True:
    try:
        item_list = item.objects.filter(status = 0)

        if len(item_list) > 0 :
            # model is not empty
            for item in item_list :
                item_data = get_data(item.link)
                new_price = int(item_data['price'])
                current_price = int(item.price)
                
                client = item.shopper
                client_email = client.email

                if new_price < current_price :
                    # price drop is valid
                    body_of_email = f"HEY {client.username}, The price of an item '{item.name}' from your bucket list has dropped from rs.{current_price} to rs.{new_price}, Go buy it up on {item.link}"
                    # send email
                    send_mail(sender="SENDER EMAIL", password="*******", body=body_of_email,
                      receiver = client_email, subject="price of an item in your bucket list has dropped.")
                pass
            pass
        else :
            # model is empty
            pass

    except TypeError:
        print(None)

    time.sleep(3600)  # AFTER every 300 seconds the code checks for the price
    pass