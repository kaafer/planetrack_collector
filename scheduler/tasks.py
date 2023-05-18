from app import db, app
from integrations.radar_integration import get_flights, build_flights_report, build_tracks_report
from models.plane import Plane
from models.track import Track
from models.validators import PlaneValidator, TrackValidator


def update_flights_information():
    with app.app_context():
        flights = get_flights()
        planes = [{
            'registration': flight.registration,
            'aircraft_code': flight.aircraft_code,
            'icao_24bit': flight.icao_24bit
        } for flight in flights]
        for plane in planes:
            plane_validated = PlaneValidator(**plane).dict()
            Plane.create(db.session, plane_validated)

        stored_planes = Plane.get_id_icao(db.session)
        print(stored_planes)

        tracks = [{
            'latitude': flight.latitude,
            'longitude': flight.longitude,
            'altitude': flight.altitude,
            'ground_speed': flight.ground_speed,
            'heading': flight.heading,
            'plane_id': (st_plane[0] for st_plane in stored_planes if st_plane[1] == flight.icao_24bit).__next__(),
        } for flight in flights]
        for track in tracks:
            track_validated = TrackValidator(**track).dict()
            Track.create(db.session, track_validated)

    return planes


def generate_report_for_all():
    tracks = Track.get_all_tracks(db.session)
    build_tracks_report(tracks)


def generate_report_for_the_moment():
    flights = get_flights()
    build_flights_report(flights)
