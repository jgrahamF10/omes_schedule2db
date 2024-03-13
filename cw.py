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


def getServiceTickets():
    try:
        resp = requests.get(
            cwUrl + f'service/Tickets?conditions=board/name="OK-OMES"%20AND%20status/name="Scheduled and assigned"'
                    f'&page=1&pagesize=1000', headers=cwHeaders)
        resp.raise_for_status()
        return resp.json()
    except Exception as Error:
        print(str(Error))
        raise


def getProjectTickets():
    try:
        resp = requests.get(
            cwUrl + f'//project/Tickets?conditions=board/name="OK-OMES Projects"%20AND%20status/name='
                    f'"Scheduled and assigned "&page=1&pagesize=1000', headers=cwHeaders)
        resp.raise_for_status()
        return resp.json()
    except Exception as Error:
        print(str(Error))
        raise


# just a test to make sure it pulls the right data
#for i in getServiceTickets():
 #   print(i['id'], i['summary'], i['status']['name'])
