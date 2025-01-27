from sqlalchemy import Column, Integer, String
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String(255), index=True)
    lname = Column(String(255), index=True)
    work_email = Column(String(255), index=True)
    email_verified = Column(String(255), index=True)
    last_login = Column(String(255), index=True)
