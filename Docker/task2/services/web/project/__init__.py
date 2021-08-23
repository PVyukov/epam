import time
import requests
import os
from flask import Flask, jsonify
from project.db_routine import create_tables, db_add_entry

app = Flask(__name__)


def get_url(api_url: str = "https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&lang=ru&units=metric&appid=8f70079acfd28fb7fc0b23b663aee176") -> (str,str):
    response = requests.get(api_url).json()
    timezone = response.get("timezone")
    temp = response.get("current").get("temp")
    return timezone, temp


create_tables()

@app.route("/")
def hello_world():
    try:
        name = os.environ['MY_NAME']
    except KeyError:
        name = "no_one"
    text = "Hello {}! The temp in {} is {} C.".format(name, *get_url())
    db_add_entry(text)
    return "This text was added to db:" + text
