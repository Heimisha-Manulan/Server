from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, validator

from modules.client import Client

app = FastAPI()

# Pydantic model for validation
class ClientCreate(BaseModel):
    first_name: str
    last_name: str
    address: Optional[str] = None
    mail: Optional[EmailStr] = None
    phone: Optional[str] = None
    referred_by: Optional[str] = None

    @validator("phone")
    def validate_phone(cls, value):
        if value and not re.match(r"^\+?\d{10,15}$", value):
            raise ValueError("Phone number must be 10-15 digits long and optionally start with +.")
        return value

class ClientUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    mail: Optional[EmailStr] = None
    phone: Optional[str] = None
    referred_by: Optional[str] = None

    @validator("phone")
    def validate_phone(cls, value):
        if value and not re.match(r"^\+?\d{10,15}$", value):
            raise ValueError("Phone number must be 10-15 digits long and optionally start with +.")
        return value

# In-memory database simulation
clients: List[Client] = []

@app.get("/clients", response_model=List[ClientCreate])
def get_all_clients():
    return clients

@app.get("/clients/{client_id}", response_model=ClientCreate)
def get_client(client_id: int):
    if client_id < 0 or client_id >= len(clients):
        raise HTTPException(status_code=404, detail="Client not found")
    return clients[client_id]

@app.post("/clients", response_model=ClientCreate, status_code=201)
def create_client(client: ClientCreate):
    new_client = Client(
        id=len(clients) + 1,
        first_name=client.first_name,
        last_name=client.last_name,
        address=client.address,
        mail=client.mail,
        phone=client.phone,
        referred_by=client.referred_by
    )
    clients.append(new_client)
    return new_client

@app.put("/clients/{client_id}", response_model=ClientCreate)
def update_client(client_id: int, client_update: ClientUpdate):
    if client_id < 0 or client_id >= len(clients):
        raise HTTPException(status_code=404, detail="Client not found")

    current_client = clients[client_id]

    # Update fields selectively
    for field, value in client_update.dict(exclude_unset=True).items():
        setattr(current_client, field, value)

    return current_client

@app.delete("/clients/{client_id}", status_code=204)
def delete_client(client_id: int):
    if client_id < 0 or client_id >= len(clients):
        raise HTTPException(status_code=404, detail="Client not found")
    clients.pop(client_id)
    return
