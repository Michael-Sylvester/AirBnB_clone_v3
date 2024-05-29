#!/usr/bin/python3
"""Module the runs the api"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.route('/')
def hello_world():
    """root response"""
    return 'Hello world'


@app.teardown_appcontext
def teardown(exception):
    """Operation to be called at the end of each request"""
    storage.close()


@app.errorhandler(404)
def handle_404(e):
    """Handle 404 errors for pages not found"""
    return jsonify({"error": "Not found"})


if __name__ == '__main__':
    import os

    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')

    app.run(host=host, port=int(port), threaded=True)
