from app import app
from flask import render_template

from scheduler.tasks import update_flights_information, generate_report_for_the_moment, generate_report_for_all


@app.route('/')
def hello():
    return render_template('greeting.html')


@app.route('/flights')
def get_flights():
    planes = update_flights_information()
    return f'Flights updated! {planes}'


@app.route('/report')
def report():
    generate_report_for_the_moment()
    return render_template('flights_in_moment.html')


@app.route('/report_all')
def report_all():
    generate_report_for_all()
    return render_template('tracks_in_moment.html')
