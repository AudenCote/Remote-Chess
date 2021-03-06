import smtplib
import time
import imaplib
import email
import email.mime.text

SMTP_SERVER = 'imap.gmail.com'

class Email:

	def __init__(self, email, password):
		self.email = email
		self.pwd = password


	def send_email(self, target, msg):
		try:
			smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
			smtp_ssl_port = 465
			username = self.email
			password = self.pwd
			sender = self.email
			targets = [target]

			msg = email.mime.text.MIMEText(msg)
			msg['Subject'] = ''
			msg['From'] = sender
			msg['To'] = ', '.join(targets)

			server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
			server.login(username, password)
			server.sendmail(sender, targets, msg.as_string())
			server.quit()
		except Exception as e:
			print(str(e))


	def read_email(self):
		try:
			mail = imaplib.IMAP4_SSL(SMTP_SERVER)
			mail.login(self.email, self.pwd)
			mail.select('inbox')

			type, data = mail.search(None, 'ALL')
			mail_ids = data[0]

			id_list = mail_ids.split()   
			latest_email_id = int(id_list[-1])

			print(mail.fetch(str(latest_email_id), '(RFC822)' )[-1][0][-1][-17:-2])


		except Exception as e:
			print(str(e))



mymail = Email('audencotechess@gmail.com', 'Pa1n!nTheAspen')

mymail.read_email()

