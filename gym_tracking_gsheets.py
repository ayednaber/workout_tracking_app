import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("gymtracking-350515-3b1794d4d0e0.json", scopes)
file = gspread.authorize(credentials)

sheet = file.open("Gym")

worksheet = sheet.worksheet("Push")

all_cells = worksheet.range('A1:C6')

for cell in all_cells:
    print(cell.value)
