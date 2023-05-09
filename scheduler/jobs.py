from apscheduler.schedulers.background import BackgroundScheduler

from app import app
from scheduler.tasks import update_flights_information


def register_radar_jobs(scheduler) -> None:
    scheduler.add_job(
        id='update_flights_info',
        func=update_flights_information,
        trigger='interval',
        minutes=app.config['UPDATE_FLIGHTS_MINUTES'],
    )
