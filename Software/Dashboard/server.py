from flask import Flask, render_template, request
import subprocess
import json
import requests

app = Flask(__name__)

@app.route('/')
def render():
 try:
    return render_template("index.html")
 except Exception as e: print(e)

@app.route('/stats')
def stats():
 try:


    res = requests.get('http://localhost:8080/2/summary')
    response = res.json()
    return response
 except Exception as e: print(e)





@app.route('/miner', methods=['GET'])
def send():

    try:
        # Set predefined commands here, only commands in this list can be executed
        if (request.args.get('command') == "restart"):
           subprocess.run(["systemctl", "restart", "miner"])

        elif (request.args.get('command') == "stop"):
            subprocess.run(["systemctl", "stop", "miner"])
        
        elif (request.args.get('command') == "start"):
             subprocess.run(["systemctl", "start", "miner"])
        elif(request.args.get('command') == "updateAddress" and request.args.get('adress')):
           with open('/miner/config.json') as f:
              data = json.load(f)
              for i in data["pools"]:
                 i["user"] = request.args.get('address')
        elif(request.args.get('command') == "updatePool" and request.args.get('adress')):
           with open('/miner/config.json') as f:
              data = json.load(f)
              for i in data["pools"]:
                 i["url"] = request.args.get('address')
                    
            
        return "ok"

    except Exception as e: print(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')