import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    response = requests.get('https://75jwlvujpd.execute-api.us-east-2.amazonaws.com/staging/expeditions/explore')
    expedition = eval(eval(response.text)['expedition'])
    message = "Sam dice que vayas a x: {}, y:{} el deposito es tiene este tamano:{}".format(expedition['x'], expedition['y'], expedition['tamano'])
 
    return "<p>Hola, {}</p>".format(message)


if __name__ == '__main__':
    app.run()