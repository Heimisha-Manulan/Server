from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database.base import Base

class SparePart(Base):
    __tablename__ = 'spare_parts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    cost = Column(Float)
    warranty = Column(Integer)


    job_spare_parts = relationship("JobSparePart", back_populates="spare_part", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<SparePart(id={self.id}, name={self.name}, cost={self.cost}, warranty={self.warranty})>"
