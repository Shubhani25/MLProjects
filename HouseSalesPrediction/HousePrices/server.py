import os
from flask import Flask, jsonify, request
import json
from HousePrices.prediction import predict

Headers = {'Content-type' : 'application/json',
            'Accept' : 'text/plain'}

def flask_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def server_is_up():
        return 'server is up'

    @app.route('/predict_price', methods = ['POST'])
    def start():
        to_predict = request.json

        print(to_predict)
        pred = predict(to_predict)
        return jsonify({"predict cost": pred})
    return app

if __name__ == '__main__':
    app = flask_app()
    app.run(debug = True, host = 'localhost')