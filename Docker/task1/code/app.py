import time
import requests
import os

#import redis
from flask import Flask

app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)
#
#def get_hit_count():
#    retries = 5
#    while True:
#        try:
#            return cache.incr('hits')
#        except redis.exceptions.ConnectionError as exc:
#            if retries == 0:
#                raise exc
#            retries -= 1
#            time.sleep(0.5)
#


def get_url(api_url: str = "https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&lang=ru&units=metric&appid=8f70079acfd28fb7fc0b23b663aee176") -> (str,str):
    response = requests.get(api_url).json()
    timezone = response.get("timezone")
    temp = response.get("current").get("temp")
    return timezone, temp



@app.route('/')
def hello():
#    count = get_hit_count()
    try:
        name = os.environ['MY_NAME']
    except KeyError: 
        name = "no_one"
    return 'Hello {}! The temp in {} is {} C .\n'.format(name, *get_url())
