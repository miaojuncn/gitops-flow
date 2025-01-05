from flask import Flask
import sys
import signal

app = Flask(__name__)


def handle_sigterm(*args):
    print("SIGTERM received. Cleaning up resources...")
    sys.exit(0)


signal.signal(signal.SIGTERM, handle_sigterm)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
