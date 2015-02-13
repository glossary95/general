from flask import Flask
app = Flask(__name__)

from flask import Blueprint

from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
