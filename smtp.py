import smtplib

# Body of the mail
content = "This email was sent using smtplib"
# Specifying smtp to use gmail server at port number : 587 (465 is also valid)
smtp = smtplib.SMTP("smtp.gmail.com" , 587)
# Initiates communication with extended smtp
smtp.ehlo()
# Starts Transport Layer Security for encryption of mailid , password 
smtp.starttls()
# Logging into mail
smtp.login("foo@gmail.com" , "foopassword")
# Sends mail from foo to bar with body as content
smtp.sendmail("foo@gmail.com" , "bar@gmail.com" , content)
# Closes the connection
smtp.close()
