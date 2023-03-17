from flask import Flask, jsonify, request
import requests
from flask_cors import cross_origin
from config import config_by_name
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config_by_name["prod"])
@app.route("/proxyAuth",methods=["POST","OPTIONS"])

@cross_origin(origins='*',methods=['POST','OPTIONS',])
def proxyAuth():
    url = config_by_name["prod"].URL
    token = config_by_name["prod"].TOKEN
    client_id = config_by_name["prod"].CLIENT_ID
    client_id_from_request = request.form.get('client_id')
    payload={}
    headers = {
        "Authorization": "Basic {}".format(token)
    }
    same = (client_id == client_id_from_request)
    if same:
        response = requests.get(url, headers=headers, data=payload)
        resp = response.json()
        return jsonify(resp), 200
    return jsonify({"msg":"Unauthorized"}),401


@app.route('/refresh_token', methods=['POST'])
def refresh_token():
    # Extract the expired access token from the request body
    expired_token = request.json.get('access_token')

    # TODO: Use your authentication logic to obtain a new access token
    url = config_by_name["prod"].URL
    token = config_by_name["prod"].TOKEN
    client_id = config_by_name["prod"].CLIENT_ID
    client_id_from_request = request.form.get('client_id')
    payload={}
    headers = {
        "Authorization": "Basic {}".format(token)
    }
    response = requests.get(url, headers=headers, data=payload)
    resp = response.json()
    new_token = resp

    # Return the new access token in the response body
    return jsonify({'access_token': new_token})


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
