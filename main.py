import mysql.connector as c
from mysql.connector import Error

con  = c.connect(host='remotemysql.com',
                database='vb3RXxTpJE',
                user='vb3RXxTpJE',
                passwd='dskEqoYNxB')
if not(con.is_connected()):
    print('An Error Occcured Come BaCK AgaIN')


cursor = con.cursor()
def homepage():
  choice = int(input('1. New User Registration\n2. LOGIN as USER\n3. LOGIN as ADMIN\nChoose Your Action:'))
  return choice
  
print("*"*110)
print(" "*45,'VACCINE LOCATION FINDER')
print("*"*110)

while True :
  choice = input('1. New User Registration\n2. LOGIN as USER\n3. LOGIN as ADMIN\n4. Exit\nChoose Your Action:')

  if choice ==  '1' :
    name = input('\nEnter Your Name: ')
    mail = input("Enter Your mail: ")
    password = 1
    pass2 = 0
    while password != pass2:
      password = input("Enter a password: ")
      pass2 = input('Re-enter your password: ')
      if password != pass2 :
        print('\nYou Failed to retype password\n')
    query = f"insert into login_details(name,mail,password) values('{name}','{mail}','{password}')"
    cursor.execute(query)
    con.commit()
    print("\nAccount Created Successfully ❤️😊\n")
    print("*"*110)
       
  elif choice == '4' :
    print("\nThanks 4 Visiting ❤️❤\n️")
    print('*'*110)
    break
    
  elif choice == '2' :
    check = 0
    hospitals = 0
    while not(check):
      mail = input('\nEnter your E-Mail: ')
      password = input("Enter Your Password: ")
      query = f"select ld.id from login_details as ld where ld. mail = '{mail}' and ld.password = '{password}' and ld.type = 'user' "
      cursor.execute(query)
      check = cursor.fetchone()
      if check : 
        print('successfully logged in 😎😎\n')
        break
      else :
        print("\nE-Mail and Password Doesn't Match ---- Please Try Again\n")
        continue
    
    while True :
      print("*"*110)
      print(' '*30,'WELCOME CHIEF VACCINATE AND MOTIVATE\n') 
      pincode = int(input('Enter pincode to search availabe Vaccination centers in your area: '))
      query = f"select vl.hospitalid ,vl.hospitalname , vl.address, vl.state, vl.pincode, vl.availabledosage  from vaccine_locations as vl where pincode = '{pincode}'"
      cursor.execute(query)
      hospitals = cursor.fetchall()
      
      if hospitals : 
        print('Here are the Vaccination Centers Near You :\n')
        for i in hospitals:
          print(f"Hospital ID : {i[0]}\nHospital Name : {i[1]}\nLocation : {i[2]}\nState : {i[3]}\nPincode : {i[4]}\nAvailable Dosage : {i[5]}\n")
        
        rev = int(input('\n-->Enter 1 to Book A SloT\n-->Enter 2 to search another location:\n-->Enter 3 to Logout'))
        if rev == 3 :
          print("*"*110)
          break
        
        elif rev == 2 :
          continue       
        elif rev == 1 :
          hc = [100]
          # hid = int(input('\nEnter Hospital ID from above available Centers: '))
          # query = f"update login_details as hl set hl.hospitalid =  {hid} where hl.mail = '{mail}' "
          # cursor.execute(query)
          # con.commit()
          # br = input("\n---Slot Successsfully Booked Press Enter to Logout---")
          
          while hc[0] > 10 :
            hid = int(input('\nEnter Hospital ID from above available Centers: '))
            testquery = f"select count(*) from login_details as ld where ld.hospitalid = {hid}"
            cursor.execute(testquery)
            hc = cursor.fetchone()
            con.commit()
            if hc[0] < 10 :
              query = f"update login_details as hl set hl.hospitalid =  {hid} where hl.mail = '{mail}' "
              cursor.execute(query)
              con.commit()
              br = input("Slot Successsfully Booked Press Enter to Logout\n")
              print("_"*100)
              if br == '':
                break
              
              else :
                print('No Slots Available in this Center select another Center ID: ')
                continue
          break
        
      else :
        print("\nSORRY NO NEARBY VACCINATION LOCATIONS FOUND\nTRy ANOTHER PINCODE")
        continue
    
    
  elif choice == '3' :
    check = 0
    while not(check):
      mail = input('\nEnter your E-Mail: ')
      password = input("Enter Your Password: ")
      query = f"select ld.id from login_details as ld where ld. mail = '{mail}' and ld.password = '{password}' and ld.type = 'admin' "
      cursor.execute(query)
      check = cursor.fetchone()
      if check : 
        print('successfully logged in 😎😎')
        break
      else :
        print("\nE-Mail and Password Doesn't Match ---- Please Try Again\n")
        continue
    
    while True :
      print("______________________________________________________")
      ac = int(input('\n-->Enter 1 to Add Vaccinations Centers:\n-->Enter 2 to Get Dosage Details:\n-->Enter 3 to Remove Vaccination Centers:\n-->Enter 4 to Logout : '))
      if ac == 4 :
        print("\nLogging out....\n")
        print("*"*110)
        break
        
      elif ac == 2 :
        dose = 0 
        query = "select vl.hospitalname, vl.availabledosage from vaccine_locations  as vl "
        cursor.execute(query)
        dose = cursor.fetchall()
        
        for i in dose :
          print(f"\nHospital Name: {i[0]}\nAvailable Dose: {i[1]}")
        br = input("\n-->Enter 1 to logout\n-->Enter any key to continue: ")
        if br == '1' :
          break
        else :
          continue
          
      elif ac == 3 :
        querys = "select vl.hospitalid, vl.hospitalname  from vaccine_locations as vl "
        cursor.execute(querys)
        s = cursor.fetchall()
        
        for i in s :
          print(f"\nHospital ID: {i[0]}\nHospital Name: {i[1]}")
          print('----------------------------------------------')
        id = int(input("Enter ID of the hospital U want To Delete: "))
        queryd = f"delete from vaccine_locations  where hospitalid = '{id}' "
        cursor.execute(queryd)
        con.commit()
        print("Selected Vaccine Location Successfully Deleted 😊")
        print('\n----------------------------------------------')
        
        br = input("-->Enter 1 to logout\nEnter any key to continue: ")
        if br == '1' :
          break
        else :
          continue
      
      elif ac == 1:
        hname = input("\nEnter Hospital Name: ")
        hstate = input("Enter State: ")
        hadd = input("Enter address: ")
        hpin = input("Enter Pincode: ")
        hdos = input("Enter Available Dosage: ")
        query = f"insert into vaccine_locations(hospitalname,state,address,pincode,availabledosage) values('{hname}','{hstate}','{hadd}','{hpin}',{hdos})"
        
        cursor.execute(query)
        print("New Center Added Successfully....")
        br = input("-->Enter 1 to logout\nEnter any key to continue: ")
        if br == '1' :
          break
        else :
          continue
      continue
         
  else :
    print('\nPlease Choose Valid Action --> Heading HOMPAGE\n')
    print("*"*110)
    continue
  
  
  
  
