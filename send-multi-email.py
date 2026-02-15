#Send Email Using Python (Single and multiple )
#Install smtplib -- library

import smtplib as s

ob= s.SMTP("SMTP.gmail.com", 587)
ob.ehlo()
ob.starttls()

ob.login("samplemail@gmail.com", "password")
subject= "Test Python"
body= "I love python"
message = "subject:{}\ n\n{}".format(subject, body)
listadd=['mail 1', 'mail 2', 'mail 3']

ob.sendmail("sender mail addr", listadd, message)
print("send mail")

ob.quit()