from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from typing import List, Optional
from datetime import date

class Base(DeclarativeBase):
    pass   

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(250), nullable=False)
    email:Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    password_hash:Mapped[str] = mapped_column(String(250), nullable=False)

    # Establish relationship between one user and many jobs
    jobs:Mapped[List['Job']] = relationship(back_populates='user')

class Job(db.Model):
    __tablename__ = 'jobs'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    company:Mapped[str] = mapped_column(String(250), nullable=False)
    role:Mapped[str] = mapped_column(String(250), nullable=False)
    status:Mapped[str] = mapped_column(String(250), nullable=False)
    url:Mapped[Optional[str]] = mapped_column(String(250))
    notes:Mapped[Optional[str]] = mapped_column(Text)
    applied_on:Mapped[Optional[date]] = mapped_column()

    # Establish relationship between jobs to one user
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    user:Mapped['User'] = relationship(back_populates='jobs')

