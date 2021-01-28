from flask import Flask, render_template, request, Response
import json
import urllib.request
from plot_tweet_stats import plot_counts, plot_average
from pandas import DataFrame
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plot-average', methods=['POST'])
def get_plot_average():
    data = request.get_json()
    return Response(plot_average(data), mimetype='image/png')


@app.route('/plot-counts', methods=['POST'])
def get_plot_counts():
    data = request.get_json()
    return Response(plot_counts(data), mimetype='image/png')


@app.route('/get-model', methods=['POST'])
def get_model():
    hashtag = request.form['hashtag']
    since = request.form['since']
    until = request.form['until']
    count = request.form['count']
    data = {
        "Inputs": {
            "inputData":
                [
                    {
                        'hashtag': hashtag,
                        'count': count,
                        'since': since,
                        'until': until,
                    },
                ],
        },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = os.getenv('API_URL')
    api_key = os.getenv('API_KEY')
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(url, body, headers)

    response = urllib.request.urlopen(req)

    result = response.read()
    df = DataFrame(json.loads(result.decode())['Results']['outputData']).to_json(date_format='iso')
    return df, 200, {
        'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run()
