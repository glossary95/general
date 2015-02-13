from flask import Blueprint
admin = Blueprint('admin', __name__, template_folder='templates_admin')

from .views import *
