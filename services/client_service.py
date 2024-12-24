from sqlalchemy.orm import Session
from models.client import Client

def create_client(session: Session, new_client: Client):
    """מוסיף לקוח חדש למסד הנתונים"""
    # new_client = Client(
    #     first_name=first_name,
    #     last_name=last_name,
    #     address=address,
    #     mail=mail,
    #     phone=phone,
    #     referred_by=referred_by
    # )
    print("add")
    session.add(new_client)
    session.commit()
    return new_client

def get_all_clients(session: Session):
    return session.query(Client).all()

def get_client_by_id(session: Session, client_id: int):
    """מחפש לקוח לפי מזהה"""
    return session.query(Client).filter(Client.id == client_id).first()

def update_client(session: Session, client_id: int, **kwargs):
    """מעודכן פרטי לקוח קיים"""
    client = get_client_by_id(session, client_id)
    if not client:
        return None
    for key, value in kwargs.items():
        if hasattr(client, key):
            setattr(client, key, value)
    session.commit()
    return client

def delete_client(session: Session, client_id: int):
    """מוחק לקוח ממסד הנתונים"""
    client = get_client_by_id(session, client_id)
    if client:
        session.delete(client)
        session.commit()
    return client
