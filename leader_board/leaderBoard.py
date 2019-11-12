import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime as date
from datetime import datetime
from random import randint
import time


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('leader_board/client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open(
    "ProtoSem.19.2_LeaderBoard").sheet1

def getToppers():
    all_data = sheet.get_all_values()
    leader_boards = []
    for i in all_data[3:]:
        leader_boards.append(i[1])
    return leader_boards[:5]
