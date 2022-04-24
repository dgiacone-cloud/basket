from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

from .tipo_features import TipoFeature


class Features(db.Base):
    __tablename__ = 'features'

    id=Column(Integer, primary_key=True)
    id_tipofeature=Column(Integer,ForeignKey("tipo_feature.id"),nullable=False)
    valor=Column(String(40),nullable=False)
    fecha_registro=Column(DateTime, server_default=func.now())
    id_documento=Column(Integer,ForeignKey("documentos.id"),nullable=False)
    en_proceso=Column(Boolean)
    comentario=Column(Text)

    def __init__(self,tipofeature, valorfeature, iddocumento, comentario):
        from .documentos import Documentos
        self.id_tipofeature=db.session.query(TipoFeature).filter(TipoFeature.nombre==tipofeature).first().id
        self.valor=valorfeature
        self.id_documento=iddocumento
        self.comentario=comentario
    