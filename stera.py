import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    response = requests.get('https://75jwlvujpd.execute-api.us-east-2.amazonaws.com/staging/expeditions')
    expedition = eval(response.text)
    message = "Sam dice que vayas a x: {}, y:{} el deposito es tiene este tamano:{}".format(expedition['x'], expedition['y'], expedition['tamano'])
    return "<p>Hola, {}</p>".format(message)
