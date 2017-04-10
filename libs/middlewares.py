# -*- coding: utf-8 -*-

from flask import request


def is_weixin(request):
    wx_ua = 'micromessenger'
    wx_work_ua = 'wxwork'
    ua = request.environ.get('HTTP_USER_AGENT', '')
    return wx_ua in ua.lower() and wx_work_ua not in ua.lower()


def is_mobile(request):
    mobile_ua = 'mobile'
    ua = request.environ.get('HTTP_USER_AGENT', '')
    return mobile_ua in ua.lower()


class RequestMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        ctx = self.app.im_self.request_context(environ)
        environ['is_mobile'] = is_mobile(ctx.request)
        environ['is_weixin'] = is_weixin(ctx.request)

        return self.app(environ, start_response)
