import smtplib
import time
import imaplib
import email
import email.mime.text
import poplib

SMTP_SERVER = 'imap.gmail.com'

class EmailNotEmail:

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

			print(mail.fetch(str(latest_email_id), '(RFC822)' )[-1][0][-1][-10:-2]) #prints last 8 figures of email body, preceded by b' and followed by '


		except Exception as e:
			print(str(e))

	@staticmethod
	def email_a_la_bin(email_info):
                
                #This function has not been tested
                
                z_string = "00000000"
                bins = [z_string[:8-len(bin(input_val)[2:])] + bin(input_val)[2:] for input_val in email_info[:-1]]

                return 'cccc' + ''.join(bins) + email_info[-1] + 'cccc'

        @staticmethod
        def bin_a_la_email(bin_string):

                #this function has not been tested

                bin_string = list(bin_string)
                i = len(bin_string)
                while i > 0:
                        if bin_string[i] == 'c':
                                bin_string.pop(i)
                        i -= 1
                bin_string = ''.join(bin_string)

                email_info = []
                for i in range(5):
                        email_info.append(int(bin_string[8*i:8+8*i], 2))

                email_info.append(bin_string([-3:]) #make sure this indexing is right



