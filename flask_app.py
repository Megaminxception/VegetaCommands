from flask import Flask
from lost_sector import today_lost_sector_vegeta
from nightfall import getNightfall


app = Flask(__name__)

@app.route("/lostsector")
def lostSector():
  return today_lost_sector_vegeta()

@app.route("/nightfall")
def nightfall():
  return getNightfall()

@app.route("/banshee")
def banshee():
  pass

@app.route("/ada")
def ada():
  pass

# Handles legacy retrievals until command is updated
@app.route("/vegeta/lostsector")
def oopsie():
  return '''If you're seeing this, this command needs to be updated!
  tell the mods to change the urlfetch to https://megaminxception.pythonanywhere.com/lostsector .
  '''



if __name__ == "__main__":
  app.run()