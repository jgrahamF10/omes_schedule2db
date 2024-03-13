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


def getSchedule():
    myCursor = sql_db.cursor()
    myCursor.execute(f"SELECT * FROM Schedule", )
    schedule = myCursor.fetchall()
    myCursor.close()
    return schedule


def addEntry(tik_num, summary, schedule_date, technician):
    myCursor = sql_db.cursor()
    try:
        sql = "INSERT INTO Schedule SET tik_num = %s, summary = %s, schedule_date = %s, technician = %s"
        val = (tik_num, summary, schedule_date, technician)
        myCursor.execute(sql, val)
        sql_db.commit()
        rows = myCursor.rowcount
        print(f"Ticket {rows} added to Schedule")  # rows will be 1 if successful
    except Exception as E:
        print(str(E))
    myCursor.close()
