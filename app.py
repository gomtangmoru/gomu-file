from flask import Flask
from blueprints.index_page import bp as index

app = Flask(__name__)

app.register_blueprint(index, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)