import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

scopes = ["http://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes= scopes)
client = gspread.authorize(creds)

sheetIdEscolas = "1S6xVW2JFyMvfSpNTDqe2UUhD4yQ44VrEvyr1KGtpgfE"
sheetEscolas = client.open_by_key(sheetIdEscolas)
dataEscolas = sheetEscolas.sheet1.get_all_records()
dataFrameEscolas = pd.DataFrame(dataEscolas)
print("Dados da pesquisa: {}".format(dataFrameEscolas.head()))
