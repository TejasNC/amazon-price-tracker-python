# amazon-price-tracker-python
This is a simple price tracker app using python that regularly compares the prices of your favorite stuff on amazon and sends you a customized notification email to tell you if the prices fell down.
This uses python and implements beautiful soup, smtplib, time and requests modules and libraries.
The libraries, modules and other tools referred during this task are as follows:
<h3>Send mail from your Gmail account using Python</h3>
<ul>
  <li><a href= "https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/">SMTPlib Tutorial</a></li>
  <li><a href= "https://realpython.com/python-send-email/">RealPython</a></li>
  <li><a href= "https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/">Free Code Camp Tutorial</a></li>
</ul>

### Instructions
<>
1. Open the folder in CMD or terminal and type `pip install -r requirements.txt`
2. Open **params.json**
3. Set **URL** to the amazon link of the product you want to track
4. Change the **Target_Price** to the price which you desire. You will recieve a mail when the price drops below this target price.
5. Set the **Sender_Email** to the Gmail with which you have configured SMTP. 
6. Enter the **SMTP Password** in **Sender_Email_Password**.
7. Find your [**user agent**](https://www.google.com/search?q=my+user+agent&oq=my+user&aqs=chrome.1.69i57j0l5.2294j1j7&sourceid=chrome&ie=UTF-8) and paste it in the **params.json** 
8. Save the file and run the script **price-tracker.py** in your terminal.
9. The script will run and check the price of the product every 24 hours. If the price drops below your target price, you will recieve an email notification. You will also recieve an email if the price changes.
10. To stop the script, close the terminal or press `ctrl+c` in the terminal. 

### Note
- This script uses Gmail's SMTP server to send the email. You can use any email server to send the email.
- You can change the time interval of checking the price by changing the `time.sleep(86400)` to any other value in **price-tracker.py**

### Reference Links
<h3>Price Tracker using Python</h3>
<ul>
  <li><a href= "https://www.geeksforgeeks.org/amazon-product-price-tracker-using-python/">Amazon Product Price Tracker- Geeks for Geeks</a></li>
  <li><a href= "https://www.scrapehero.com/tutorial-how-to-scrape-amazon-seller-prices-using-python/">Scape Hero Tutorial</a></li>
  </ul>
