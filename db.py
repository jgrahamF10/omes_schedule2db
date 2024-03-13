import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()

sql_db = mysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    database=os.getenv('DB_NAME'),
    port=os.getenv('DB_PORT')
)


def checkDupe(tikNum):
    myCursor = sql_db.cursor()
    myCursor.execute(f"SELECT * FROM Schedule where ticket_num = {tikNum}", )
    schedule = myCursor.fetchall()
    myCursor.close()
    if schedule:
        return True
    else:
        return False


def addEntry(tik_num, summary, schedule_date, technician):
    myCursor = sql_db.cursor()
    try:
        sql = "INSERT INTO Schedule SET ticket_num = %s, summary = %s, schedule_date = %s, technician = %s"
        val = (tik_num, summary, schedule_date, technician)
        myCursor.execute(sql, val)
        sql_db.commit()
        rows = myCursor.rowcount
        if rows == 1: # rows will be 1 if successful
            print(f"Ticket {tik_num} added to Schedule")  
    except Exception as E:
        print(str(E))
    myCursor.close()
