from typing import Union
import os

from pydantic_settings import BaseSettings
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
# from sqlalchemy_utils import database_exists, create_database

class Settings(BaseSettings):
    version: str = "0.1.0"
    title: str = "Vestir API"
    api_prefix: str = "/api/v1"
    session: Union[Session, None] = None
    engine: Union[Engine, None] = None

    def __init__(self):
        super().__init__()

        db_url = f"postgresql+psycopg2://{os.getenv('DB_USER', 'postgres')}:{os.getenv('DB_PASSWORD', 'postgres')}@{os.getenv('DB_SERVICE','postgresdb')}/{os.getenv('DB_NAME','vestir')}"

        self.engine = create_engine(db_url)
        # # if not database_exists(self.engine.url):
        # #     create_database(self.engine.url)
        self.session = Session(self.engine)



settings = Settings()