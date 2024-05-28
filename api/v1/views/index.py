#!/usr/bin/python3
"""Index module"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def json_status():
    """Return satus of the api"""
    return jsonify({"status": "ok"})
