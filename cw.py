import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

'''Hedader Data'''
cwToken = os.getenv('CWToken')
# This is the ConnectWise access code generated earlier

cwUrl = "https://api-na.myconnectwise.net/v4_6_release/apis/3.0/"
# check the URL matches your region, look at your CW Manage login box if not

cwHeaders = {"Authorization": "Basic " + cwToken,
             "clientID": os.getenv('clientID'),
             "Content-Type": "application/json"}


def getTickets():
    tickets = []
    try:
        serviceResp = requests.get(
            cwUrl + f'service/Tickets?conditions=board/name="OK-OMES"%20AND%20status/name="Scheduled and assigned"'
                    f'&page=1&pagesize=1000', headers=cwHeaders)
        serviceResp.raise_for_status()
        tickets.extend(serviceResp.json())
    except Exception as Error:
        print(str(Error))
        raise
    try:
        projectResp = requests.get(
            cwUrl + f'//project/Tickets?conditions=board/name="OK-OMES Projects"%20AND%20status/name='
                    f'"Scheduled and assigned "&page=1&pagesize=1000', headers=cwHeaders)
        projectResp.raise_for_status()
        tickets.extend(projectResp.json())
    except Exception as Error:
        print(str(Error))
        raise
    return tickets


def getSchedule(tikNum):
    try:
        resp = requests.get(
            cwUrl + f'/schedule/entries?conditions=objectId={tikNum}', headers=cwHeaders)
        resp.raise_for_status()
        return resp.json()
    except Exception as Error:
        print(str(Error))
        raise


# just a test to make sure it pulls the right data
# for i in getTickets():
#     #print(i['id'], i['summary'], i['status'])
#     schedule = getSchedule(i['id'])[0]
#     print(schedule['member']['name'], schedule['dateStart'])
#     break
