from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey , Numeric, Date
from sqlalchemy.orm import sessionmaker, relationship

class OutCards(db.Base):
        __tablename__ = 'out_cards'
        key=Column(Integer, primary_key=True)
        id=Column(String(60))
        nombre=Column(String(60))
        expediente=Column(String(60))
        rol=Column(String(60))
        vehiculo=Column(String(60))
        lesiones=Column(String(60))
        abogado=Column(String(60))
        fecha=Column(Date)

        def __init__(self, id, nombre, expediente, rol, vehiculo, lesiones, abogado, fecha):
            self.id=id
            self.nombre=nombre
            self.expediente=expediente
            self.rol=rol
            self.vehiculo=vehiculo
            self.lesiones=lesiones
            self.abogado=abogado
            self.fecha=fecha    
        