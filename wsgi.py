import sys

from loguru import logger

logger.configure(
    handlers=[
        dict(sink=sys.stderr,
             backtrace=False,
             diagnose=False,
             format="[{time}] {level: <8} | {extra[context]} - {message}"),

    ],
    extra={"context": "App"},
)

from flask import Flask
from application import create_app, socketio

app: Flask = create_app()

if __name__ == '__main__':
    socketio.run(app=app, host='0.0.0.0', port=80, log_output=True, debug=True, use_reloader=False)
