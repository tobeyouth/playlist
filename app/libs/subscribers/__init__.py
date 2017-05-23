# -*- coding: utf-8 -*-

from flask import request_started, request
from user_agents import parse


def connect_request(app):
    for func in [bind_ua]:
        request_started.connect(func, app)


def bind_ua(sender, **extra):
    user_agent = request.headers.get('User-Agent', '')
    request.user_agent = parse(user_agent)
