print ("                                       Wel Come to Booking.com---Hotels mode")
from checker_sql import checker
import datetime
from datetime import date
import MySQLdb

db = MySQLdb.connect("localhost","root","root","hoteldb" )
rec=db.cursor()
sql="select * from tenants"
try:
  rec.execute(sql)
  results=rec.fetchall()
  for row in results:
    print(row[6])
    l=row[6].split("-")
    d1=date(int(l[0]),int(l[1]),int(l[2]))
    d2=date.today()
    d=d1-d2
    print(d)
    print(d.days)
    if d.days==0:
      sql="update suprabat_rooms set booked='no' where roomnumber='%d'"%(row[1])
      sql1="delete from tenants where userid='%d'"%(row[0])
      try:
         rec.execute(sql)
         db.commit()
         rec.execute(sql1)
         db.commit()
      except:
         db.rollback()
         print("UNABLE TO UPDATE")
except:
 db.rollback()
 print("UNABLE TO UPDATE")
up=int(raw_input("1.Sign Up \n 2.Login \n 3.forgot password\n "))
username=""
if up==1:             
   obj=checker()
   obj.setname(raw_input("enter the username: "))
   obj.setmail(raw_input("enter the mail: "))
   obj.setmobile_no(raw_input('enter the mobile no: '))
   obj.setplace(raw_input('enter the native place: '))
   pass1=raw_input("enter the password: ")
   pass2=raw_input("Re enter the password: ")
   obj.setpassword(pass1,pass2)
   username=obj.username
   sql1 = "insert into users(username,password,mailid,mobile,place) values('%s','%s','%s','%d','%s')"%(obj.username,obj.password,obj.mail,int(obj.mobile_no),obj.place)
   try:
     rec.execute(sql1)
     db.commit()
     print("successfully inserted")
   except:
     db.rollback()
     print(" unable to insert new user")
   states="succ"

elif up==2:
   username=raw_input("enter username :")
   password=raw_input("enter password :")
   sql="select * from users where username='%s' and password='%s'"%(username,password)
   rec.execute(sql)
   result=rec.fetchall()
   while len(result)==0:     
      print("Invalid account")
      username=raw_input("enter username :")
      password=raw_input("enter password :")
      sql="select * from users where username='%s' and password='%s'"%(username,password)
      rec.execute(sql)
      result=rec.fetchall()
   else:
      states="succ"
      if len(result)!=0:
        record=result[0]
        uid=record[0]
        print("fdssdfs",uid) 
   
  
else:
        forgot=int(raw_input("Did you forget password Enter 1 for yes"))
        if forgot==1:
           username=raw_input("enter your username")
           phno=int(raw_input("enter the mobile number which you have used for registation"))
           #print username
           sql="select * from users where username='%s' and mobile='%d'"%(username,phno)
           try:
                rec.execute(sql)
                db.commit()
           except:
                db.rollback()
           mno=rec.fetchall()
           if mno!=0:
              password=raw_input("enter the new password")
              sql="update users set password='%s' where mobile='%d'"%(password,phno)
              try:
                rec.execute(sql)
                db.commit()
                states="succ"
              except:
                db.rollback()
                print("unable to update password")
           else:
              print("Invalid user")
              states="not succ"
if states=='succ': 
  while(1):
   slt=int(raw_input("1.Hotel Suprabat\n 2.Hotel Haritha\n 3. logout"))
   if slt==1:
      cost=0
      print("1.signle bed rooms\n 2.double bed rooms\n")
      roomtype=int(raw_input("please select room type"))
      if roomtype==1: roomtype1="single bed room"
      else: roomtype1="double bed room"
      aminity=int(raw_input("1.AC\n 2.Non AC\n please enter AC or Non AC\n"))
      if aminity==1: amty="AC"
      else:amty="NON AC"
      sql="select roomnumber,roomtype,aminity,cost from suprabat_rooms where booked='no' and roomtype='"+roomtype1+"' and aminity='"+amty+"'" 
      try:
         rec.execute(sql)
         db.commit()
      except:
         db.rollback()
         print(" error ----------122-------")
      recs=rec.fetchall()
      for row in recs:
         print(row[0],"  ",row[1],"   ",row[2],"   ",row[3],"\n")
         cost=row[3]
      roomid=int(raw_input("enter room number"))
      days=int(raw_input("enter no of days"))
      print("you have selected ",type,"with ",amty," for ",days,"days room cost is : ",days*cost)
      sql="insert into tenants(roomnumber,tenantname,room_type,aminity,booked_date,left_date,amount_paid)values('%d','%s','%s','%s','%s','%s','%d')"%(roomid,username,roomtype1,amty,str(date.today()),str(date.today()+datetime.timedelta(days)),days*cost)
      try:
        rec.execute(sql)
        db.commit()
      except:
        db.rollback()
        print("UNABLE TO INSERT RECORD INTO TENANTS TABLE")
      sql="update suprabat_rooms set booked='YES' where roomnumber='%d'"%(roomid)
      print(sql)
      try:
        rec.execute(sql)
        db.commit()
      except:
        db.rollback()
        print("UNABLE TO UPDATE SUPRABAT_ROOMS TABLE")

      print("thank you")
   elif slt==2:
      print("Haritha is not yet implemented")
   elif slt==3:
      break	
db.close()





