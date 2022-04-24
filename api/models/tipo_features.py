from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import sessionmaker, relationship


class TipoFeature(db.Base):
        __tablename__ = 'tipo_feature'
        id=Column(Integer,primary_key=True)
        nombre=Column(String(40), nullable=False, unique=True)
    
        features= relationship("Features", backref="features", lazy=True,foreign_keys="Features.id_tipofeature")
        def __init__(self, nombre):
                self.nombre=nombre