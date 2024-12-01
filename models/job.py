from sqlalchemy import Column, Integer, String, ForeignKey
from database.base import Base
from sqlalchemy.orm import relationship

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(255))
    client_id = Column(Integer, ForeignKey('clients.id'))
    total = Column(Integer)
    net_total = Column(Integer)

    client = relationship("Client", back_populates="jobs")

    spare_parts = relationship(
    "JobSparePart", back_populates="job", cascade="all, delete-orphan"
)
    def __repr__(self):
        return (f"<Job(id={self.id}, description={self.description}, "
                f"client_id={self.client_id}, total={self.total}, net_total={self.net_total})>")
