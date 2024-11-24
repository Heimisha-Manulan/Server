from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from .interface import DatabaseInterface

class MySQLDatabase(DatabaseInterface):
    def __init__(self, user, password, host, database):
        self.database_url = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        self.engine = None
        self.Session = None

    def connect(self):
        self.engine = create_engine(self.database_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        if not self.engine:
            raise Exception("Database not connected. Call connect() first.")
        Base.metadata.create_all(self.engine)
