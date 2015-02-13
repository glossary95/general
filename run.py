from flask import Flask
from flask.ext.bootstrap import Bootstrap
from app import app


if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True)
    #general.run(host='0.0.0.0', port = 80, debug = True)