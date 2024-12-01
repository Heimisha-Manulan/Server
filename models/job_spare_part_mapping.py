from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

class JobSparePart(Base):
    __tablename__ = 'job_spare_parts_mapping'

    job_id = Column(Integer, ForeignKey('jobs.id'), primary_key=True)
    spare_part_id = Column(Integer, ForeignKey('spare_parts.id'), primary_key=True)
    count = Column(Integer)

    job = relationship("Job")

    spare_part = relationship(
    "SparePart", back_populates="job_spare_parts"
)

    def __repr__(self):
        return f"<JobSparePart(job_id={self.job_id}, spare_part_id={self.spare_part_id}, count={self.count})>"
