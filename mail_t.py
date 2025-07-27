import smtplib
a="omkarsawant2277@gmail.com"
sender = 'rerstaurantbill1@gmail.com'
receivers = [a]

b="password trial"
message = b

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except:
   print ("Error: unable to send email")