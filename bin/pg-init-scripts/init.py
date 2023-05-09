from sqlite3 import IntegrityError
from sqlalchemy import sql


def init_db():
    from app import db
    try:
        with open('schema.sql', mode='r') as f:
            db.session.execute(sql.text(f.read()))
            db.session.commit()

    except IntegrityError:
        db.session.rollback()


if __name__ == '__main__':
    from app import app

    with app.app_context():
        connection_uri = app.config.get('SQLALCHEMY_DATABASE_URI')
        """Initializes the database."""
        init_db()
        print('Initialized the database.')
