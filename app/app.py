from flask import Flask
from threading import Event
import signal

from flask_kafka import FlaskKafka
app = Flask(__name__)

INTERRUPT_EVENT = Event()

bus = FlaskKafka(INTERRUPT_EVENT,
                 bootstrap_servers=",".join(["172.17.0.1:9091"])
                 )


def listen_kill_server():
    signal.signal(signal.SIGTERM, bus.interrupted_process)
    signal.signal(signal.SIGINT, bus.interrupted_process)
    signal.signal(signal.SIGQUIT, bus.interrupted_process)
    signal.signal(signal.SIGHUP, bus.interrupted_process)


@bus.handle('books')
def test_topic_handler(msg):
    print(msg)


if __name__ == '__main__':
    bus.run()
    listen_kill_server()
    app.run(debug=True, port=5004)
