import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Faith Etornam'
email['to'] = 'faithgbadegbe1@gmail.com'
email['subject'] = 'You are Spider-Man'

email.set_content('I am a Python Developer')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('faithgbadegbe1@gmail.com', '')
    smtp.send_message(email)
    print('all good Spidey')