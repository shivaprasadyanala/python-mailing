# # Import the following module
from email.mime.text import MIMEText
# # from email.mime.image import MIMEImage
# from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
# import smtplib
# import os

# # initialize connection to our
# # email server, we will use gmail here
# smtp = smtplib.SMTP('smtp.gmail.com', 25)
# smtp.ehlo()
# smtp.starttls()

# # Login with your email and password
# smtp.login('shivaprasadyanala@gmail.com','shivaprasad@123')


# # send our email message 'msg' to our boss
# def message(subject="secret key",
# 			text="", img=None,
# 			attachment=None):
	
# 	# build message contents
# 	msg = MIMEMultipart()
	
# 	# Add Subject
# 	msg['Subject'] = subject
	
# 	# Add text contents
# 	msg.attach(MIMEText(text))
# 	print("hi")
	
# 	return msg


# # Call the message function
# msg = message("hello this is secret key")
# print("msg",msg)
# # Make a list of emails, where you wanna send mail
# to = ["shivaprasad99@gmail.com"]

# # Provide some data to the sendmail function!
# smtp.sendmail(from_addr="hello@gmail.com",
# 			to_addrs=to, msg=msg.as_string())

# # Finally, don't forget to close the connection
# smtp.quit()




import smtplib
import random
import re
my_email = "shivaprasadyanala@gmail.com"
rec_emil = "shivaprasadysp99@gmail.com"
password = "lsyzetmlkptpxhse"

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$&@?<>~!%#";
hasUpper = False
hasLower = False
hasDigit = False
hasSpecial = False

secpass = ""


while True:
	randpass = ""
	for x in range(8):
		ch = random.choice(symbols)
		# print(ch.upper(),ch.lower())
		if(ch.isupper()):
			hasUpper = True
		elif(ch.islower()):
			hasLower = True
		elif(ch.isdigit()):
			hasDigit = True
		else:
			hasSpecial = True
		randpass+=ch;
	if hasUpper and hasLower and hasDigit and hasSpecial:
		print(randpass)
		secpass = randpass
		break


msg = MIMEMultipart()
      
subject = "secret password for login"
# Add Subject
msg['Subject'] = subject  
  
# Add text contents
text = "the secret password is: "+secpass
msg.attach(MIMEText(text)) 
message = msg;
# message = message("the secret password is: "+secpass)

# message['Subject'] = "secret key"

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
	connection.starttls()
	connection.login(user=my_email, password=password)
	connection.sendmail(
	    from_addr=my_email,
	    to_addrs=rec_emil,
	    msg=message.as_string()
	    )


 
# randpass = ""
# def isspecial(ch):
# 	if(ch =='!' or ch == '@' or ch == '#' or ch == '%' or ch == '$' or ch =='?' or ch =='"' or ch =='~' or ch == '<' or ch =='>' ):
# 		return True
# 	return False;



# print(randpass)