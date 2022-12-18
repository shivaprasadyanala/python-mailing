from flask import Flask
from flask_mail import Mail, Message
import mysql.connector


app =Flask(__name__)
app.app_context().push()
import random
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'shivaprasadyanala@gmail.com'
app.config['MAIL_PASSWORD'] = 'lsyzetmlkptpxhse'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)




db=mysql.connector.connect(user="root",passwd="root",host="localhost",port=3000,database="crudmvc") 
 
my_cursor=db.cursor() #getting the cursor object
#this query will return a email whose isadmin is true
my_cursor.execute("select email from users where isadmin='true'") #creating the database named students
user = my_cursor.fetchone()


# mail = user[0]
# print(mail)


symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$&@?<>~!%#";
hasUpper = False
hasLower = False
hasDigit = False
hasSpecial = False

secpass = ""
msg = Message('Hello', sender = 'shivaprasadyanala@gmail.com', recipients = [f'{user[0]}'])
# msg.body = "Hello Flask message sent from Flask-Mail"
while True:
	randpass = ""
	for x in range(12):
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

msg.body = "hello this is a secret key: "+secpass
msg.subject = "secret key"
mail.send(msg)
print("msg sent")

