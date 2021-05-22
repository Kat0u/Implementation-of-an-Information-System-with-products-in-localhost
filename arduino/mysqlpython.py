import mysql.connector
from mysql.connector import Error
import time
import serial

try:
    connection = mysql.connector.connect(host='localhost',database='eshop',user='root',password='')
    a = [1] * 3
    b=-1
    q=0

    ser = serial.Serial('COM4', 9800, timeout=1)
    time.sleep(3)

    while True:
       

        connection = mysql.connector.connect(host='localhost',database='eshop',user='root',password='')           
                         
                       


        if(connection.is_connected()):
          db_Info = connection.get_server_info()
          print ("Syndethika se sql server ")
          cursor = connection.cursor()
          cursor.execute("select database();")
          record = cursor.fetchone()
          print ( " Syndethika me vash " )                   
          state = "SELECT * FROM proionta"
          cursor.execute(state)
          records = cursor.fetchall()
          for record in records:
            a[q]=record[b]
            q+=1
            b=sum(a)

          if( connection.is_connected()):
                           
                               
                           if b >= 80:
                              time.sleep(5)
                              ser.write(b'H')
                              time.sleep(5)
                              ser.write(b'L')
                              print("STATE 1")
                           
                           elif b> 40:
                              
                              time.sleep(2)
                              ser.write(b'H')
                              time.sleep(2)
                              ser.write(b'L')
                              print("STATE 2")
                           else:
                              ser.write(b'H')
                              time.sleep(1)
                              ser.write(b'L')
                              time.sleep(1)
                              print("STATE 3")
                              
                              
                              update1 = ("UPDATE proionta SET apothema=apothema+1 WHERE id='1'")
                              update2 = ("UPDATE proionta SET apothema=apothema+1 WHERE id='2'")
                              update3 = ("UPDATE proionta SET apothema=apothema+1 WHERE id='3'")
                              cursor.execute(update1)
                              cursor.execute(update2)
                              cursor.execute(update3)
                              connection.commit()
                              cursor.close()
                              connection.close()

                         
finally:
        
         cursor.close()
         connection.close()
         
