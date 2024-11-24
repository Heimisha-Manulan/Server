from modules import Client
from database import MySQLDatabase

def setup_database(database_type, **kwargs):
    db = None
    if database_type == "mysql":
        db = MySQLDatabase(**kwargs)
    else:
        raise ValueError("Unsupported database type.")

    db.connect()
    db.create_tables()
    print(f"Tables created successfully in {database_type} database.")
    return db

if __name__ == "__main__":
    # דוגמה לחיבור למסד נתונים MySQL
    mysql_db = setup_database("mysql", user="ruth", password="ruthH0533137873", host="localhost", database="heimisha_manulan")

