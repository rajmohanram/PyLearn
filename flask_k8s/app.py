from flask import Flask, render_template
from flask import request
import socket
from os import environ

app = Flask(__name__)


@app.route('/')
def index():
    if request.headers.getlist("X-Forwarded-For"):
        x_fwd_for = request.headers.getlist("X-Forwarded-For")[0]
    else:
        x_fwd_for = None
    content = {
        'svc_name': environ.get('SERVICE_NAME'),
        'node_name': environ.get('NODE_NAME'),
        'node_ip': environ.get('NODE_IP'),
        'pod_name': socket.gethostname(),
        'pod_ip': environ.get('POD_IP'),
        'pod_namespace': environ.get('POD_NAMESPACE'),
        'src_ip': request.remote_addr,
        'x_fwd_for': x_fwd_for
    }
    return render_template('index.html', **content)


if __name__ == '__main__':
    app.run()