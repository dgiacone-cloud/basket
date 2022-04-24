from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import sessionmaker, relationship

class Juzgados(db.Base):
        __tablename__ = 'juzgados'
        id=Column(Integer,primary_key=True)
        nombre=Column(String(40), nullable=False, unique=True)
        id_fuero=Column(Integer,ForeignKey("fueros.id"),nullable=False)
        id_distrito=Column(Integer,ForeignKey("distritos.id"),nullable=False)
        id_provincia=Column(Integer,ForeignKey("provincias.id"),nullable=False)

        # No utilizamos relaciones pues estas tablas deberian poblarse desde
        # formularios desde los cuales y avendria el id de las FKeys.
        # Entonces no es necesario en el _init_ buscar el ID
        
        def __init__(self, nombre, id_fuero, id_distrito, id_provincia):
                self.nombre=nombre
                self.id_fuero=id_fuero
                self.id_distrito=id_distrito
                self.id_provincia=id_provincia

