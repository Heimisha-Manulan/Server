from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from .interface import DatabaseInterface

class MySQLDatabase(DatabaseInterface):
    def __init__(self, user, password, host, database):
        """Initializes the MySQL database connection parameters."""
        self.database_url = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        self.engine = None
        self.Session = None

    def connect(self):
        """Establishes a connection to the MySQL database."""
        self.engine = create_engine(self.database_url, pool_pre_ping=True)  # Added pool_pre_ping for connection reliability
        self.Session = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

    def create_tables(self):
        """Creates all tables defined in the Base metadata."""
        if not self.engine:
            raise Exception("Database not connected. Call connect() first.")
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """Provides a session for interacting with the database."""
        if not self.Session:
            raise Exception("Session factory not initialized. Call connect() first.")
        return self.Session()
    
  

    def dispose(self):
        """Disposes the engine and releases all resources."""
        if self.engine:
            self.engine.dispose()
        self.engine = None
        self.Session = None
