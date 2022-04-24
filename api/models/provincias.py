from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import sessionmaker, relationship

class Provincias(db.Base):
        __tablename__ = 'provincias'
        id=Column(Integer,primary_key=True)
        nombre=Column(String(40), nullable=False, unique=True)
        Juzgados= relationship("Juzgados", backref="juzgados", lazy=True,foreign_keys="Juzgados.id_provincia")
        
        def __init__(self, nombre):
                self.nombre=nombre