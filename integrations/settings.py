import pathlib

from pydantic.env_settings import BaseSettings

import config


class Settings(BaseSettings):
    radar_login: str = config.DevelopmentConfig.RADAR_LOGIN
    radar_password: str = config.DevelopmentConfig.RADAR_PASSWORD
    aria: str = config.DevelopmentConfig.ARIA
    PROJECT_ROOT_PATH = pathlib.Path(__file__).parent.parent
    TEMPLATES_PATH = PROJECT_ROOT_PATH / 'app' / 'templates'

    class Config:
        case_sensitive = False
        env_file = '../.env'
        env_file_encoding = 'utf-8'


settings = Settings()
