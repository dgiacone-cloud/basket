from .import  db
from sqlalchemy import Column, Integer, String, Float

class PreSiniestros(db.Base):
        __tablename__ = 'pre_siniestros'
        key=Column(Integer, primary_key=True)
        expediente=Column(String(255))
        origen_base=Column(String(255))
        feature=Column(String(255))
        valor=Column(String(255))
        info_extra=Column(String(255))

        def __init__(self,expediente,origen,feature,valor,info_extra):
                self.expediente=expediente
                self.origen=origen
                self.feature=feature
                self.valor=valor
                self.info_extra=info_extra
                

        