from flask import Flask, request, session, Response
from lost_sector import today_lost_sector_vegeta
from nightfall import getNightfall
import requests
from api_key import groupme_bot_id
import datetime
from crown_bot import handle_chat


app = Flask(__name__)

app.secret_key = "please help lmfao"


@app.route("/lostsector")
def lostSector():
    return today_lost_sector_vegeta()


@app.route("/nightfall")
def nightfall():
    return getNightfall()

# Handles legacy retrievals until command is updated


@app.route("/vegeta/lostsector")
def oopsie():
    return '''If you're seeing this, this command needs to be updated!
  tell the mods to change the urlfetch to https://megaminxception.pythonanywhere.com/lostsector .
  '''


@app.route("/crown", methods=['POST', 'GET'])
def crown():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return Response(status=400)

        result = handle_chat(data)

        if result == None:
            return Response(status=202)

        url = "https://api.groupme.com/v3/bots/post"
        json = {'bot_id': groupme_bot_id, 'text': result}

        requests.post(url, json=json)
        return Response(status=200)

    return Response(status=202)


if __name__ == "__main__":
    app.run()
