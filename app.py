from flask import Flask
from blueprints.index import bp as index
from blueprints.upload import bp as upload
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

app.register_blueprint(index, url_prefix='/')
app.register_blueprint(upload, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)