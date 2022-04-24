from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import sessionmaker, relationship

class TipoSiniestro(db.Base):
        __tablename__ = 'tipo_siniestro'
        id=Column(Integer,primary_key=True)
        nombre=Column(String(40), nullable=False, unique=True)
        siniestros=  relationship("Siniestros", backref="tipo_siniestro", lazy=True)

        def __init__(self, nombre):
                self.nombre=nombre