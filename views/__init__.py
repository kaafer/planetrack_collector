from flask import Blueprint

routes = Blueprint('routes', __name__)

from .view import *
