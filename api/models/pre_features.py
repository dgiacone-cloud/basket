from .import  db
from sqlalchemy import Column, Integer, String, Float

class PreFeatures(db.Base):
        __tablename__ = 'pre_features'
        key=Column(Integer, primary_key=True)
        id=Column(String(255))
        expediente=Column(String(255))
        feature=Column(String(255))
        valor=Column(String(255))
        origen_base=Column(String(255))

        def __init__(self,id,nombre,dni,domicilio,origen):

                self.id=id
                self.expediente=expediente
                self.feature=feature
                self.valor=valor
                self.origen_base=origen