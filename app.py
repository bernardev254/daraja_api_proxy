from flask import Flask, jsonify, request
import requests
from flask_cors import cross_origin
from config import config_by_name
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config_by_name["prod"])

@app.route('/generate', methods=['POST', 'GET','OPTIONS'])
@cross_origin(origins='*',methods=['POST','GET','OPTIONS',])
def generate():
    url = config_by_name["prod"].URL
    token = config_by_name["prod"].TOKEN
    #client_id = config_by_name["prod"].CLIENT_ID
    #client_id_from_request = request.form.get('client_id')
    payload={}
    headers = {
        "Authorization": "Basic {}".format(token)
    }
    response = requests.get(url, headers=headers, data=payload)
    resp = response.json()
    

    # Return the new access token in the response body
    return jsonify(resp)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
