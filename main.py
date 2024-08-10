import gspread
from google.oauth2.service_account import Credentials
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Scopes required for the Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']

# Path to your Service Account JSON file from environment variable
CREDS_JSON = os.getenv('CREDS_JSON')

# User and Message from environment variables
user = os.getenv('USER_NAME')
msg = os.getenv('MESSAGE')
textArr = [user, msg]

def authenticate_google_sheets():
    creds = Credentials.from_service_account_file(CREDS_JSON, scopes=SCOPES)
    client = gspread.authorize(creds)
    return client

def update_google_sheet(text):
    client = authenticate_google_sheets()
    # Open the sheet
    sheet = client.open("test").worksheet("Sheet1")

    # Update the specific cell at row 2, column 1 (e.g., A2)
    sheet.update_cell(2, 1, text[0])
    sheet.update_cell(2, 2, text[1])
    print(f"Successfully inserted {text[0]} and {text[1]} into the sheet.")

if __name__ == '__main__':
    update_google_sheet(textArr)
