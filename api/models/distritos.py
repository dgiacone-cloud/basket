from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import sessionmaker, relationship

class Distritos(db.Base):
        __tablename__ = 'distritos'
        id=Column(Integer,primary_key=True)
        nombre=Column(String(40), nullable=False, unique=True)
        Juzgados= relationship("Juzgados", backref="distritos", lazy=True)

        def __init__(self, nombre):
                self.nombre=nombre