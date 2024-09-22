from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app import app, db


class Book(db.Model):
    """Create a books table"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    review = db.Column(db.String(400), unique=False, nullable=True)




with app.app_context():
    db.create_all()
