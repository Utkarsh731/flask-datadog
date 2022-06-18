from flask import Flask
import requests
from ddtrace import tracer
from operator import itemgetter


app = Flask(__name__)

@tracer.wrap(name='my_resource1')
@app.route("/api")
def hello_world():
    response = requests.get("https://api.covidtracking.com/v1/us/daily.json")
    response = response.json()
    response = sorted(response,key=itemgetter("date"))
    return_response = []
    for data in response:
        return_response.append({"date":data["date"],"positive":data["positive"]})
    return {"data": return_response}

if __name__ == "__main__":
    app.run()

