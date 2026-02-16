#Share Msg on WhatsApp Automatically 
#install 

import pywhatkit as pyw
import datetime
# pyw.sendwhatmsg('Receier No', 'Msg Here!','time in 24 hr format', 'minute')



now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 2


pyw.sendwhatmsg('+917798641400', 'This is ai generated msg', hour, minute)
