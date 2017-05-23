# -*- coding:utf-8 -*-

from flask import render_template, request, url_for
from .homepage import index


def init_web(app):

    app.add_template_global(url_for, 'url_for')
    app.add_url_rule('/', 'index', index)

    @app.errorhandler(404)
    def exist(e):
        context = {
            'referrer': request.referrer
        }
        return render_template('404.html', **context), e.code
    return app
