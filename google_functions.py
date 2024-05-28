import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Google_API/client_secret.json', scope)
client = gspread.authorize(creds)

def getsheet(sheetname):
    # Find a workbook by name and open the first sheet
    try:
        gsheet = client.open(sheetname).sheet1
        return gsheet
    except:
        print('Failed to load sheet')


def gsheet2df(gsheet):
    try:
        gsheet_list = gsheet.get_all_values()
        columnnames = gsheet_list.pop(0)
        df = pd.DataFrame(gsheet_list, columns=columnnames)
        return df
    except:
        print('Failed to get data')



