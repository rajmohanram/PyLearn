from flask import Flask
from flask import request
from flask import jsonify
import socket
import os

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/", methods=["GET"])
def get_my_ip():
    return jsonify({
        'node_ip': os.environ.get('NODE_IP'),
        'pod_name': socket.gethostname(),
        'pod_namespace': os.environ.get('POD_NAMESPACE'),
        'pod_ip': os.environ.get('POD_IP'),
        'client_ip': request.remote_addr
    }), 200


if __name__ == "__main__":
    app.run()