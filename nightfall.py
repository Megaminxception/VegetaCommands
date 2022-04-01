import requests
import sqlite3
import json
from api_key import getKey

def getNightfall():
  HEADERS = {"X-API-key":getKey()} # Keeps my API key hidden :D

  r = requests.get("https://www.bungie.net/Platform/Destiny2/Milestones/", headers=HEADERS)

  # Handling API issues in a more elegant way
  if r.status_code != 200:
    return f"""Oh no! The Bungie API is acting a little weird right now, please
     try again in a bit (Status code {r.status_code})."""

  nightfall = r.json()

  nf_hash_fake = nightfall['Response']['1942283261']['activities'][0]['activityHash']

  id = int(nf_hash_fake)
  if (id & (1 << (32 - 1))) != 0:
    id = id - (1 << 32)

  database = "world_sql_content_0f66fd1549744b23bb5d9f51c8603eaa.sqlite3"
  datab = sqlite3.connect(database)
  cursor = datab.cursor()
  cursor.execute('''
  SELECT * FROM DestinyActivityDefinition WHERE id =?
  ''', (id,))
  datab.commit()
  result = cursor.fetchall()
  datab.close()
  nf = json.loads(result[0][1])['displayProperties']['description']
  # adding more for bot to say
  full_text = "This week's Nightfall is " + nf + "!"
  return full_text

# For testing
print (getNightfall())