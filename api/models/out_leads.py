from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey , Numeric, BigInteger, SmallInteger
from sqlalchemy.orm import sessionmaker, relationship

class OutLeads(db.Base):
        __tablename__ = 'out_leads'
        key=Column(Integer, primary_key=True)
        id=Column(String(60))
        nombre=Column(String(60))
        dni=Column(BigInteger)
        frecuencia=Column(SmallInteger)
        mult_roles=Column(SmallInteger)
        mult_aseg=Column(SmallInteger)
        mult_abog=Column(SmallInteger)
        score=Column(Numeric(precision=10, scale=2, asdecimal=True))

        def __init__(self, id,nombre,dni,frecuencia,mult_roles,mult_aseg,mult_abog,score):
                self.id=id
                self.nombre=nombre
                self.dni=dni
                self.frecuencia=frecuencia
                self.mult_roles=mult_roles
                self.mult_Aseg=mult_aseg
                self.mult_abog=mult_abog
                self.score=score



        