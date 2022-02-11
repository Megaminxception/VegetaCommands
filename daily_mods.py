import requests
import sqlite3
import json
from api_key import getKey

HEADERS = {"X-API-key":getKey()}

def getBanshee():
  banshee_hash = "672118013"
  r = requests.get(f"https://www.bungie.net/Platform/Destiny2/2/Profile/4611686018452692662/Character/2305843009619685244/Vendors/{banshee_hash}/?components=402", headers=HEADERS)

  banshee = r.json()
  print(banshee)

  mod1 = banshee['29']['itemHash']
  mod2 = banshee['30']['itemHash']
  print(mod1)
  print(mod2)

def getAda():
  ada_hash = ""
  pass

getBanshee()