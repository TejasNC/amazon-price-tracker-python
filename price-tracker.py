# import required files and modules
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import os
import json

#Open the params.json file
with open('params.json','r') as file:
    params = json.load(file)
    
headers = {
    "User-Agent": params['User-Agent']
}

# send a request to fetch HTML of the page
response = requests.get(params["URL"], headers=headers)

# create the soup object
soup = BeautifulSoup(response.content, 'html.parser')

# change the encoding to utf-8
soup.encode('utf-8')

#print(soup.prettify())

# function to check if the price has dropped below 20,000
def check_price(prev_price=0):
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(class_ = "a-price-whole").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
  #print(price)

  #converting the string amount to float
  converted_price = float(price[0:5])
  print(converted_price)
  
  if(converted_price < params['Target_Price']):
    send_mail(converted_price, below_budget=True)
  else:
    # print('Price is still high')
    if prev_price==0:
      send_mail(converted_price, below_budget=False)
    else:
      diff = prev_price - converted_price #if price has risen, then the diff will be negative
      send_mail(diff, below_budget=False)
  #using strip to remove extra spaces in the title
  prev_price = converted_price
  print(title.strip())




# function that sends an email if the prices fell down
def send_mail(diff,below_budget=True):
  
  if below_budget:
    
    server = smtplib.SMTP('smtp.gmail.com', 587)    
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(params["Sender_Email"], params["Sender_Email_Password"])   #enter sender email id and sender email id password

    subject = 'Price Has Fallen Down Below Target!'
    URL = params["URL"]
    body = f"Check the amazon link {URL}"

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
      params["Sender_Email"],   # enter sender email id
      params["Reciever_Email"], # enter receiver email id
      msg                   # message that is to be sent
    )
    #print a message to check if the email has been sent
    print('Hey Email has been sent')
    # quit the server
    server.quit()

  if not below_budget:

    if (diff<0):
      subject = f'Price Has Risen By {(-1*diff)}!'
      URL = params["URL"]
      body = f"Check the amazon link {URL}"
    elif(diff>0):
      subject = f'Price Has Fallen By {diff}!'
      URL = params["URL"]
      body = f"Check the amazon link {URL}"   
    else:
      return 
        
    print('Price is still higher than Target Price')
    server = smtplib.SMTP('smtp.gmail.com', 587)    
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(params["Sender_Email"], params["Sender_Email_Password"])   #enter sender email id and sender email id password
      
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
      params["Sender_Email"],   # enter sender email id
      params["Receiver_Email"], # enter receiver email id
      msg                   # message that is to be sent
    )
    #print a message to check if the email has been sent
    print('Hey Email has been sent')
    # quit the server
    server.quit()
    
#loop that allows the program to regularly check for prices
prev_price = 0 
while(True):
  check_price(prev_price)
  time.sleep(params['Time_Interval']) # the time after which you want the program to check the price in seconds. It is currently set to 1 day