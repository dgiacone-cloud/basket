from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import sessionmaker, relationship


class Vehiculos(db.Base):
        __tablename__ = 'vehiculos'
        id=Column(Integer,autoincrement=True,primary_key=True)
        dominio=Column(String(10),nullable=False,unique=False)
        id_documento=Column(Integer,ForeignKey("documentos.id"),nullable=False)
        marca=Column(String(100))

        def __init__(self, iddocumento,dominio,marca):
                from .documentos import Documentos
                self.dominio=dominio
                self.id_documento=db.session.query(Documentos).filter(Documentos.iddocumento==iddocumento).first().id
                self.marca=marca