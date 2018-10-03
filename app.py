from flask import Flask, request, make_response
import subprocess

app = Flask(__name__)


"""
Если запрос неправильный- вернем 404
"""

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


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
