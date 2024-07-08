import logging
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

CREDENTIALS_FILE = 'tgbot.json'
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')


logging.basicConfig(level=logging.INFO)

def get_sheet_data(range_name):
    # Аутентификация и создание объекта для доступа к Google Sheets API
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    print(range_name)
    # Получение данных из таблицы
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
    values = result.get('values', [])
    
    if not values:
        return 'No data found.'
    else:
        return values[0][0]   

#Создание объекта для доступа к Google Sheets API
def get_sheet_service():
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE)
    service = build('sheets', 'v4', credentials=creds)
    return service.spreadsheets()

def get_next_empty_row_in_column(sheet, column):
    # Получаем данные столбца "B"
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=column).execute()
    values = result.get('values', [])   
    # Определяем следующую пустую строку
    next_empty_row = len(values) + 1
    return next_empty_row

#Добавление данных в таблицу
def append_sheet_data(values, range_name):
    sheet = get_sheet_service()
    # Получаем следующую пустую строку
    next_empty_row = get_next_empty_row_in_column(sheet, column=range_name)
    new_range_name = range_name.split(':')[0] + str(next_empty_row)
    body = {
        'values': values
    }
    result = sheet.values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=new_range_name,
        valueInputOption='RAW',
        # insertDataOption='INSERT_ROWS',
        body=body
    ).execute()
    return result
