import os


class BaseConfig:
    HOST = '0.0.0.0'
    LOCAL_HOST = os.environ.get('LOCAL_HOST', 'http://0.0.0.0')
    LOCAL_PORT = os.environ.get('LOCAL_PORT', '5000')
    APP_URL = os.environ.get('APP_URL', 'https://url_example.com')

    DEBUG = False
    TESTING = False

    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5433')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'dev')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # SCHEDULER #
    UPDATE_FLIGHTS_MINUTES = 1


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    RADAR_LOGIN = os.environ.get('RADAR_LOGIN')
    RADAR_PASSWORD = os.environ.get('RADAR_PASSWORD')
    ARIA = os.environ.get('TRACKING_ARIA', "60.016,59.682,29.978,30.57")  ##Pulkovo


class ProductionConfig(BaseConfig):
    HOST = '0.0.0.0'
    PORT = 5000
