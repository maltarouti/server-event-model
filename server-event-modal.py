import time

from flask import Flask
from flask import Response


app = Flask(__name__)


@app.route('/sse')
def sse():
    counter = 0

    def generate():
        nonlocal counter
        while True:
            data = 'data: Counter: {}\n\n'.format(counter)
            counter += 1
            yield data
            time.sleep(1)

    return Response(generate(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run(port=8888, debug=True)
