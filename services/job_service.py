from sqlalchemy.orm import Session
from models.job import Job

def create_job(session: Session, new_job: Job):
    """Adds a new job to the database."""
    session.add(new_job)
    session.commit()
    return new_job

def get_job(session: Session, job_id: int):
    """Retrieves a job from the database by its ID."""
    return session.query(Job).filter(Job.id == job_id).first()

def update_job(session: Session, job_id: int, updated_job: Job):
    """Updates an existing job in the database."""
    job = session.query(Job).filter(Job.id == job_id).first()
    if job:
        job.title = updated_job.title
        job.description = updated_job.description
        job.salary = updated_job.salary
        session.commit()
    return job

def delete_job(session: Session, job_id: int):
    """Deletes a job from the database by its ID."""
    job = session.query(Job).filter(Job.id == job_id).first()
    if job:
        session.delete(job)
        session.commit()
    return job

def get_jobs(session: Session):
    """Retrieves all jobs from the database."""
    return session.query(Job).all()

def get_jobs_by_client_id(session: Session, client_id: int):
    """Retrieves jobs associated with a specific client ID."""
    return session.query(Job).filter(Job.client_id == client_id).all()
