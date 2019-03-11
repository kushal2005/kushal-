#email
import smtplib
try:
	s=smtplib.SMTP('smtp.gmial.com','587')
	s.starttls()
	sender='kushalr.18bcs@cmr.edu.in.com'
	receiver='kushilikehormavu@gmail.com'
	msg="hii"
	s.login(sender,'8197871227')
	s.sendmail(sender,receiver,msg)
except:
    print("some error occured")
else:
    print("msg sent sucessfully")
    s.quit()    	

