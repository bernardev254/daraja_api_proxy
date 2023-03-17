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
    #url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
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

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
