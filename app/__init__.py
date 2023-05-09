import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

app = Flask(__name__)

app.config['ERROR_404_HELP'] = False
conf = os.environ.get('FLASK_ENV', 'config.DevelopmentConfig')
app.config.from_object(conf)
print(f"Started APP, DB connect: {app.config.get('SQLALCHEMY_DATABASE_URI')}")

db = SQLAlchemy(app)

from views import *

app.register_blueprint(routes)

from scheduler import Scheduler

Scheduler({'apscheduler.timezone': 'UTC'}, background=True).start()

print("Scheduler registered")
print(f"Interval: {app.config.get('UPDATE_FLIGHTS_MINUTES')}")
