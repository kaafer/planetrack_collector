from app import db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


class Plane(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    registration = db.Column(db.VARCHAR(20))
    aircraft_code = db.Column(db.VARCHAR(20))
    icao_24bit = db.Column(db.VARCHAR(20))

    def __repr__(self):
        return f'<Plane {self.name}>'

    @classmethod
    def get_id_icao(cls, session: Session):
        return session.query(Plane.id, Plane.icao_24bit).select_from(Plane).all()

    @classmethod
    def create(cls, session: Session, data: dict) -> 'Plane':
        instance = Plane(**data)
        try:
            session.add(instance)
            session.commit()
        except IntegrityError as e:
            # if plane already exists & e == "sqlalchemy.exc.IntegrityError":
            print(e)
            session.rollback()
        except Exception as e:
            session.rollback()
            raise e
        return instance
