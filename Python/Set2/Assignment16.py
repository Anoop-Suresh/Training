import smtplib

content =' This is Anoop from python'

mail= smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('anoopsuresh.sayonetech@gmail.com','*******')

mail.sendmail('anoopsuresh.sayonetech@gmail.com','anoopsuresh.ust@gmail.com',content)

mail.close()