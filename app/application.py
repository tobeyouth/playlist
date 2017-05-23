# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
from views import init_web
from libs.subscribers import connect_request
from libs.middlewares import RequestMiddleware


def create_app(debug=False):
    app = Flask(__name__)

    app.debug = debug

    init_web(app)
    connect_request(app)

    app.wsgi_app = RequestMiddleware(app.wsgi_app)

    return app


app = create_app(True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
