import gspread
from google.oauth2.service_account import Credentials


scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("automacao-frequencia.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1VOAVrJqMkjMZm_JIdrjULo1R4EPrDhpnm7oCc6MkoxQ"
sheet = client.open_by_key(sheet_id)
value_list = sheet.sheet1.row_values(1)
print(value_list)