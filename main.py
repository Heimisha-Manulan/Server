from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.base import Base
from models import Client, Job, SparePart, JobSparePart
from services import get_jobs_by_client_id, get_jobs, create_job, delete_job, get_job
from services.client_service import create_client, delete_client, get_all_clients, get_client_by_id


def main():
    # Create an engine to connect to your database using PyMySQL
    # engine = create_engine('mysql://ruth:ruthH0533137873@localhost/heimisha_manulan')
    engine = create_engine('mysql+pymysql://ruth:ruthH0533137873@localhost/heimisha_manulan')

    Base.metadata.bind = engine

    # Create a session to interact with the database
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    try:
        # # Create a new Client instance and populate its attributes
        # new_client = Client( first_name='John', last_name='Doe', address='123 Main St', mail='john.doe@example.com', phone='1234567890', referred_by='Google' ) 
        # session.add(new_client)
        # # new_client = Client(name='John Doe')
        # # Add the new Client instance to the session and commit the transaction
        # # session.add(new_client)
        # session.commit()

        # print("New Client instance inserted successfully.")

        # # Create a new Job instance associated with the client
        # new_job = Job(description='Software Developer', client=new_client, total = 400, net_total = 200)

        # # Add the new Job instance to the session and commit the transaction
        # session.add(new_job)
        # session.commit()
        # print(new_job)
        # print("New Job instance inserted successfully.")

        print(get_jobs(session))

        # # Create a new SparePart instance associated with the job
        # new_sparepart = SparePart(name='Keyboard', cost = 50,  warranty = 5)

        # # Add the new SparePart instance to the session and commit the transaction
        # session.add(new_sparepart)
        # session.commit()

        # print("New SparePart instance inserted successfully.")

        # new_job_spart_part = JobSparePart(job = new_job, spare_part = new_sparepart, count = 2)
        # session.add(new_job_spart_part)
        # session.commit()

        # print(new_job_spart_part)

    except Exception as e:
        print(f"Error inserting instances: {str(e)}")
        session.rollback()

    finally:
        session.close()

if __name__ == "__main__":
    main()

# Example usage



