from .import  db

from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import sessionmaker, relationship

class TipoClientes(db.Base):
        __tablename__ = 'tipo_cliente'
        id=Column(Integer,primary_key=True)
        nombre=Column(String(40), nullable=False, unique=True)
        clientes= relationship("Clientes", backref="clientes", lazy=True,foreign_keys="Clientes.id_tipocliente")

        def __init__(self, nombre):
                self.nombre=nombre