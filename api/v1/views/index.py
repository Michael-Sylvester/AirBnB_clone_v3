#!/usr/bin/python3
"""Index module"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

classes = {0: "amenities", 1: "cities", 2: "places",
           3: "reviews", 4: "states", 5: "users"}


@app_views.route('/status')
def json_status():
    """Return satus of the api"""
    return jsonify({"status": "ok"})


@app_views.route('/stats')
def view_stats():
    """Return the stats of the api"""
    count_obj = {}
    for index in range(0, len(classes)):
        count_obj[classes[index]] = storage.count(classes[index])
    return count_obj

@app_views.errorhandler(404)
def handle_404(e):
    return jsonify({"error": "Not found"})