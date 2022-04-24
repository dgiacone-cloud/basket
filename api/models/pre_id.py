from .import  db
from sqlalchemy import Column, Integer, String, Float
 
class PreId(db.Base):
        __tablename__ = 'pre_id'
        key=Column(Integer, primary_key=True)
        id = Column(String(255))
        nombre=Column(String(255))
        dni=Column(String(40))
        domicilio=Column(String(255))
        origen_base=Column(String(255))

        def __init__(self,id,nombre,dni,domicilio,origen):
                
                self.id=id
                self.nombre=nombre
                self.dni=dni
                self.domicilio=domicilio
                self.origen=origen
    