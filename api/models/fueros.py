from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import sessionmaker, relationship

class Fueros(db.Base):
        __tablename__ = 'fueros'
        id=Column(Integer,primary_key=True)
        nombre=Column(String(40), nullable=False, unique=True)
        Juzgados= relationship("Juzgados", backref="Fueros", lazy=True,foreign_keys="Juzgados.id_fuero")

        def __init__(self, nombre):
                self.nombre=nombre