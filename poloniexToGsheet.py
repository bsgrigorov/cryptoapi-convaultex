from poloniex import Poloniex
import os
# check out https://github.com/burnash/gspread
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# you will need to add environment variables that contain the
# poloniex api key and secret
api_key = os.environ.get('POLONIEX_API_KEY')
api_secret = os.environ.get('POLONIEX_SECRET')
polo = Poloniex(api_key, api_secret)

def getTotalBtcValue():
	balances = polo.returnCompleteBalances()
	btcValue = 0
	for cur in balances:
		data = balances[cur]
		btcValue += data["btcValue"]

	return btcValue

def openSlushPoolSheet():
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	return client.open("Automated Investors P/L").sheet1

def recordTotalBtcValueInGsheet(sheet, totalBtcValue):
	sheet.update_cell(2, 4, totalBtcValue)


btcValue = getTotalBtcValue()
sheet = openSlushPoolSheet()
recordTotalBtcValueInGsheet(sheet, btcValue)
print "Recorded Total BTC value: " + str(btcValue) + " in gsheet"
