from cw import getTickets, getSchedule
import db
from pprint import pprint
from dateutil.parser import parse
from datetime import datetime, timedelta
import schedule
from time import sleep


def main():
    #Read in data
    complete_data = getTickets()
    
    #Extract Specific Data (ticket_num, summary, schedule_date, technician)
    for data in complete_data:
        if "Scheduled and assigned " in data['status']['name']:
            ticket_num = data['id']
            if not db.checkDupe(ticket_num):
                installSched = getSchedule(data['id'])[0]
                summary = data['summary']
                tech = installSched['member']['name']
                instalDate = parse(installSched['dateStart']).strftime("%Y-%m-%d %H:%M:%S")
                try:
                    db.addEntry(ticket_num, summary, instalDate, tech)
                except Exception as E:
                    print(E)

    print(f"Done {(datetime.now() - timedelta(hours=5)).strftime("%m/%d/%Y, %H:%M")}")

schedule.every(4).hours.do(main)

if '__name__' == main():
    main()
    while True:
        schedule.run_pending()
        sleep(1)