from flask import Flask, render_template, request
import subprocess
import json
import requests

app = Flask(__name__)

@app.route('/')
def render():
 try:
    data = {}
    res = requests.get('http://techy.ddns.net:11898/info')
    response = res.json()
    data["networkHashrate"] = response["hashrate"]
    data["networkDifficulty"] = response["difficulty"]
    data["networkHeight"] = response["height"]

    res = requests.get('http://localhost:8080/2/summary')
    response = res.json()
    data["averageHashrate"] = response["hashrate"]["total"][0]
    data["acceptedShares"] = response["connection"]["accepted"]
    data["rejectedShares"] = response["connection"]["rejected"]
    print(data)
    return render_template("index.html", data=data)
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
                    
        else:
            stdout, stderr = (b"command not found", b"")
            
        return "ok"

    except Exception as e: print(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')