import mysql.connector
DB=mysql.connector.connect(host="localhost",username="tstuser",password="Ftm4linux")
myCursor=DB.cursor()

try:
    myCursor.execute("UPDATE FTM.CHANNEL SET LOG_DATA='Y', LOG_TXN ='Y', VALIDATE_ISF = 3,  VALIDATE_MSG=3 WHERE 1 =1")
    print("updated")
except Exception as e:
    print("error", e)
    