from typing import Optional

import pandas as pd
from FlightRadar24.api import FlightRadar24API
from ydata_profiling import ProfileReport

from integrations.settings import settings

fr_api = FlightRadar24API()
# let_me_be_in = fr_api.login(settings.radar_login, settings.radar_password) #TODO: make it once
flight_details_headers = ["registration", "aircraft_code", "icao_24bit", "latitude", "longitude", "altitude",
                          "ground_speed", "heading"]
track_details_headers = ["created_date", "latitude", "longitude", "altitude", "ground_speed", "heading"]


def get_flights():
    flights = fr_api.get_flights(bounds=settings.aria)
    return flights


def build_flights_report(flights: Optional[dict] = None):
    df = pd.DataFrame(
        [[
            flight.registration,
            flight.aircraft_code,
            flight.icao_24bit,
            flight.latitude,
            flight.longitude,
            flight.get_altitude(),
            flight.get_ground_speed(),
            flight.get_heading()
        ] for flight in flights],
        columns=flight_details_headers)
    profile = ProfileReport(df, title="Flights In Moment Report")
    profile.to_file(settings.TEMPLATES_PATH / "flights_in_moment.html")


def build_tracks_report(tracks: Optional[dict] = None):
    df = pd.DataFrame(
        [[
            track.created_date,
            track.latitude,
            track.longitude,
            track.altitude,
            track.ground_speed,
            track.heading,
        ] for track in tracks],
        columns=track_details_headers)
    profile = ProfileReport(df, title="Tracks Overall Report")
    profile.to_file(settings.TEMPLATES_PATH / "tracks_in_moment.html")
