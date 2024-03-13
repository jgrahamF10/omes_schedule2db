from cw import getServiceTickets
import db
from pprint import pprint

if __name__ == '__main__':
    #FIXME Loop for every service ticket

    #Read in data
    complete_data = getServiceTickets()
    
    #Extract Specific Data (ticket_num, summary, schedule_date, technician)
    for data in complete_data:
        ticket_num = data['id']
        summary = data['summary']
        schedule_date = data[]
        technician = 
        #print(data['id'])

    #for data in complete_data:
        #print(data)
'''if data == 'workRole':
            print("JOE SMOE\n\n")'''

print("Done")
    #pprint(complete_data)
    
    
    
    
    
    
    #Service_ID = 

    #Export that specific data to the database