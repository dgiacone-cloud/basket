from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey , BigInteger
from sqlalchemy.orm import sessionmaker, relationship

class Personas(db.Base):
        __tablename__ = 'personas'

        id=Column(Integer, primary_key=True)
        nu_dni=Column(BigInteger,nullable=True, unique=False, index=True)
        clase=Column(Integer)
        nombre=Column(String(200),nullable=False, unique=False)
        nombre_ordenado=Column(String(200))
        domicilio=Column(String(250),nullable=False, unique=False)

        def __init__(self,nu_dni,nombre,domicilio):

                self.nu_dni=nu_dni,
                self.clase=0
                self.nombre=nombre.lower()
                self.nombre_ordenado=self.ordena_nombre(nombre)
                self.domicilio=domicilio
        def ordena_nombre(self,nombre):
                lista=nombre.lower().split()
                lista.sort()
                nombre_ordenado=""
                for valor in lista:
                        nombre_ordenado=nombre_ordenado+" "+valor
                return nombre_ordenado


        
        
