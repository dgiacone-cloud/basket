from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

class TipoDocumento(db.Base):
        __tablename__ = 'tipo_documento'
        id=Column(Integer,primary_key=True)
        nombre=Column(String(40), nullable=False, unique=True)
        codigo_doc=Column(String(4), nullable=False, unique=True)

        documentos= relationship("Documentos", backref="tipo_documento", lazy=True,foreign_keys="Documentos.id_tipodocumento")

        def __init__(self,nombre,codigo):
                  self.nombre=nombre
                  self.codigo=codigo
