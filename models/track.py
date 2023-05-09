from app import db

from sqlalchemy.orm import Session


class Track(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    created_date = db.Column(db.DateTime)
    latitude = db.Column(db.FLOAT)
    longitude = db.Column(db.FLOAT)
    altitude = db.Column(db.INTEGER)
    ground_speed = db.Column(db.INTEGER)
    heading = db.Column(db.INTEGER)
    plane_id = db.Column(db.ForeignKey('plane.id'))

    def __repr__(self):
        return f'<Track {self.created_date}>'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'created_date': self.created_date,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'altitude': self.altitude,
            'ground_speed': self.ground_speed,
            'heading': self.heading,
            'plane_id': self.plane_id
        }

    @classmethod
    def get_all_tracks(cls, session: Session):
        return session.query(
            Track.created_date,
            Track.latitude,
            Track.longitude,
            Track.altitude,
            Track.ground_speed,
            Track.heading,
        ).select_from(Track).all()

    @classmethod
    def create(cls, session: Session, data: dict) -> 'Track':
        instance = Track(**data)
        try:
            session.add(instance)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        return instance
