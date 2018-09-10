from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def get_ip():
    return request.remote_addr, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
