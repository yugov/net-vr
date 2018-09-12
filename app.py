from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route('/myip', methods=["GET"])
def get_ip():
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0], 200
    else:
        return request.remote_addr, 200


@app.route('/tracert', methods=["GET"])
def get_traceroute():
    if len(request.args) == 0:
        ip = get_ip()[0]
        traceroute = subprocess.check_output(['traceroute', ip])
        return traceroute, 200
    else:
        ip = request.args.get('ip')
        traceroute = subprocess.check_output(['traceroute', ip])
        return traceroute, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
