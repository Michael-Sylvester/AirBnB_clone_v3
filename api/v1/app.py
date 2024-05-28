#!/usr/bin/python3
"""Module the runs the api"""

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask()
app.register_blueprint(app_views)


@app.route('/')
def hello_world():
    """root response"""
    return 'Hello world'


@app.teardown_appcontext
def teardown(exception):
    """Operation to be called at the end of each request"""
    storage.close()


if __name__ == '__main__':
    import os

    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')

    app.run(host=host, port=int(port), threaded=True)
