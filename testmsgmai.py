import smtplib
from email.message import EmailMessage
#from smtplib import SMTP


text="Test Mail"
receiver_mail="shubhamrane09@gmail.com"
subject="Test"


try:

   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login('shubhamrane09@gmail.com', '$hubhaM01')
   email = EmailMessage()
   email['From'] = 'mail@gmail.com'
   email['To'] = receiver_mail
   email['Subject'] = subject
   email.set_content(text)
   server.send_message(email)
except:
   print ("Error: unable to send email")