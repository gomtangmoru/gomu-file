from flask import Flask
from blueprints.index import bp as index
from blueprints.config import bp as config
from modules import Auto_cleaner
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

app.register_blueprint(index, url_prefix='/')
app.register_blueprint(config, url_prefix='/')

if __name__ == '__main__':
    Auto_cleaner = Auto_cleaner()
    Auto_cleaner.start()
    try:
        app.run(debug=False)
    except KeyboardInterrupt:
        Auto_cleaner.stop()
        logger.info("강제적으로 중단됨")    
