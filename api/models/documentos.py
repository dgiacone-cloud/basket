from .import  db
import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey , Numeric, Date, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

# Importo las clases que necesito para el __init__
from .juzgados import Juzgados
from .tipo_documentos import TipoDocumento
from .clientes import Clientes
from .siniestros import Siniestros
from .vehiculos import Vehiculos
from .features import Features
from .roles import Roles

class Documentos(db.Base):
    __tablename__ = 'documentos'

    id=Column(Integer, primary_key=True)
    iddocumento=Column(String(300))
    fecha_creacion=Column(DateTime,server_default=func.now())
    fecha_registro=Column(DateTime,server_default=func.now())
    fecha_ocr=Column(DateTime)
    numeroexpediente=Column(String(100))
    codigo_lote=Column(String(100))
    id_juzgado=Column(Integer,ForeignKey("juzgados.id"),nullable=True)
    id_tipodocumento=Column(Integer,ForeignKey("tipo_documento.id"),nullable=True)
    id_cliente=Column(Integer,ForeignKey("clientes.id"),nullable=True)
    nombre_archivo_origen=Column(String(300))
    id_elastic=Column(String(100))
    en_proceso=Column(Boolean)
    origen=Column(String(40))
    juzgado=Column(String(100))
    fuero=Column(String(100))
    abogado=Column(String(100))
    cuil_abogado=Column(String(100))
    categorizacion=Column(String(100))
    
    
    # Defino las relaciones
  

    siniestros= relationship("Siniestros", backref="documentos", lazy=True)
    vehiculos= relationship("Vehiculos", backref="documentos",lazy=True)
    features= relationship("Features", backref="Documentos", lazy=True)
    roles= relationship("Roles", backref="Documentos", lazy=True)
  
        

    def __init__(self,iddocumento,tipodocumento,cliente,nombre_archivo_origen,id_elastic,origen):
           
            self.iddocumento=iddocumento
            # self.fecha_ocr=fecha_ocr
            # self.numero_palabras=numeropalabras
            # self.numeroexpediente=numeroexpediente
            # self.numeroSiniestro=numeroSiniestro
            # self.id_juzgado=db.session.query(Juzgados).filter(Juzgados.nombre==juzgado).first().id
            self.id_tipodocumento=db.session.query(TipoDocumento).filter(TipoDocumento.nombre==tipodocumento).first().id
            #self.id_cliente=db.session.query(Clientes).filter(Clientes.razon_social==cliente).first().id
            self.nombre_archivo_origen=nombre_archivo_origen
            self.id_elastic=id_elastic
            self.origen=origen