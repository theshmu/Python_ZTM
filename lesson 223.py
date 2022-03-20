import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Shmuel Cohen'
email['to'] = 'amitfriedman9393@gmail.com'
email['subject'] = 'You WONNNNNNN (Totally not spam)'

#email.set_content('Non HTML message')
email.set_content(html.substitute({'name': 'Puchi'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pythonudemythrowaway@gmail.com', 'sgf9gGkj')
    smtp.send_message(email)
    print('Message sent')
