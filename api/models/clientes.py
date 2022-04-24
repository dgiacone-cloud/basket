from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey

from .tipo_clientes import TipoClientes

class Clientes(db.Base):

    __tablename__ = 'clientes'
    id=Column(Integer, primary_key=True)
    razon_social=Column(String(100), nullable=False, unique=True)
    direccion=Column(String(100),nullable=True, unique=False)
    contacto=Column(String(100),nullable=True, unique=False)
    email=Column(String(100),nullable=True, unique=False)
    numero_cuit=Column(Integer)
    id_tipocliente=Column(Integer,ForeignKey("tipo_cliente.id"),nullable=False)

    def __init__(self, razon_social,tipocliente):
         self.razon_social=razon_social
         #self.direccion=direccion
         #self.contacto=contacto
         #self.email=email
         #self.numero_cuit=numero_cuit
         self.id_tipocliente=db.session.query(TipoClientes).filter(TipoClientes.nombre==tipocliente).first().id