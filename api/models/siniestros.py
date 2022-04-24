from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey , Numeric, Date, Boolean,DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
#from documentos import Documentos
from .tipo_siniestros import TipoSiniestro

class Siniestros(db.Base):
    __tablename__ = 'siniestros'

    id=Column(Integer, primary_key=True)
    id_tiposiniestro=Column(Integer,ForeignKey("tipo_siniestro.id"),nullable=False)
    id_documento=Column(Integer,ForeignKey("documentos.id"),nullable=False)
    numeroSiniestro=Column(String(100),nullable=False)
    fecha_registro=Column(DateTime, server_default=func.now())
    en_proceso=Column(Boolean)

    def __init__(self,tiposiniestro,iddocumento,numerosiniestro):

        self.id_documento=db.session.query(Documentos).filter(Documentos.id==iddocumento).first().id
        self.id_tiposiniestro=db.session.query(TipoSiniestro).filter(TipoSiniestro.nombre==tiposiniestro).first().id
        self.numeroSiniestro=numerosiniestro