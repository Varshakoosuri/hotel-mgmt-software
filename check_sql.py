import re
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
#from sql_reg import Registation
#from hotels_list import Ratna
database = MySQLdb.connect("localhost","root","root","hoteldb" )
crs=database.cursor()
class checker:
        def setname(self,value):
                sql="select username from users where username='%s'"%value
                crs.execute(sql)
                result=crs.fetchall()
                if value.isalnum()==True and len(result)==0:self.username=value
                else:self.setname(raw_input("** invalid username or user name already exist **\n please enter different username: "))
        def setmail(self,value):
                if value.endswith('.com') and value.find('@')>0:self.mail=value
                else:self.setmail(raw_input("plz enter valid mail id: "))
        def setmobile_no(self,value):
                if value.isdigit()==True and len(value)==10 or len(value)==8:self.mobile_no=value
                else:self.setmobile_no(raw_input("plz enter valid mobile no: "))
        def setpassword(self,x,y):
                f=0
                if(re.search("\w+",x)!=None):
                        if(re.search("[A-Z]",x)!=None):
                                if(re.search("\W",x)!=None):
                                        if x==y:
                                                self.password=x
                                                f=1
                                        else:
                                                print("confirm password and password not match")
						
						
				else:
					print("one symbol is req")
			else:
				print("password must have one uppercase letter")
		else:
			print("one alphabet and digit req")
		if f==0:
			x=raw_input("enter password")
			y=raw_input("enter confirm password")
			self.setpassword(x,y)
	def writepassword(self,username,password,mail,mobile_no):
           self.username=username
           self.password=password
           self.mail=mail
           self.mobile_no=mobile_no
	def setplace(self,value):
           if value.isalpha()==True:self.place=value
           else:self.setplace(raw_input("plz enter valid place:"))
#if __name__=='__main__':
 #     chk=checker()
  #    #name=
   #   chk.validname(raw_input("enter the username: ")) 
      
