# import re

# class Client:
#     def __init__(self, id=None, first_name=None, last_name=None, address=None, mail=None, phone=None, referred_by=None):
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = address
#         self.mail = mail
#         self.phone = phone
#         self.referred_by = referred_by
#         self.validate_email()
#         self.validate_phone()

#     def validate_email(self):
#         if self.mail and not re.match(r"[^@]+@[^@]+\.[^@]+", self.mail):
#             raise ValueError(f"Invalid email address: {self.mail}")

#     def validate_phone(self):
#         if self.phone and not re.match(r"^\+?\d{10,15}$", self.phone):  # example: validate phone as digits
#             raise ValueError(f"Invalid phone number: {self.phone}")

#     def __str__(self):
#         return (f"Client ID: {self.id or 'N/A'}, Name: {self.first_name or 'N/A'} {self.last_name or 'N/A'}, "
#                 f"Address: {self.address or 'N/A'}, Email: {self.mail or 'N/A'}, Phone: {self.phone or 'N/A'}, "
#                 f"Referred By: {self.referred_by or 'N/A'}")
#     def __repr__(self):
#         return (f"Client(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, "
#                 f"address={self.address}, mail={self.mail}, phone={self.phone}, referred_by={self.referred_by})")
from sqlalchemy import Column, Integer, String
from database.base import Base
from sqlalchemy.orm import relationship


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    address = Column(String(255))
    mail = Column(String(100))
    phone = Column(String(15))
    referred_by = Column(String(50))

    jobs = relationship("Job", back_populates="client")

    def __repr__(self):
        return (f"<Client(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, "
                f"address={self.address}, mail={self.mail}, phone={self.phone}, referred_by={self.referred_by})>")
