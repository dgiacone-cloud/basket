from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey , Numeric, Date, Boolean,DateTime,BigInteger,Text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

from .tipo_roles import TipoRol

 

class Roles(db.Base):
    __tablename__ = 'roles'

    id=Column(Integer, primary_key=True)
    id_tiporol=Column(Integer,ForeignKey("tipo_rol.id"),nullable=False)
    id_documento=Column(Integer,ForeignKey("documentos.id"),nullable=False)
    nu_dni=Column(BigInteger,index=True) 
    valor=Column(String(100),nullable=False)
    fecha_registro=Column(DateTime, server_default=func.now())
    en_proceso=Column(Boolean)
    comentario=Column(Text)

    def __init__(self,tiporol, iddocumento, nu_dni,valorfeature,comentario):
        from .documentos import Documentos
        self.id_tiporol=db.session.query(TipoRol).filter(TipoRol.nombre==tiporol).first().id
        self.id_documento=db.session.query(Documentos).filter(Documentos.id==iddocumento).first().id
        self.nu_dni=nu_dni
        self.valor=valorfeature
        self.comentario=comentario
    
    