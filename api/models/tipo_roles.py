from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import sessionmaker, relationship

class TipoRol(db.Base):
        __tablename__ = 'tipo_rol'
        id=Column(Integer,primary_key=True)
        nombre=Column(String(40), nullable=False, unique=True)
        roles= relationship("Roles", backref="roles", lazy=True,foreign_keys="Roles.id_tiporol")

        def __init__(self, nombre):
                self.nombre=nombre