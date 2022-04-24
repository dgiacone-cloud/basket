from .import  db
from sqlalchemy import Column, Integer, String, Float
 
class PreAutorizados(db.Base):
        __tablename__ = 'pre_autorizados'
        key=Column(Integer, primary_key=True)
        document_id=Column(String(255))
        nombre=Column(String(255))
        dni=Column(String(255))
        rol=Column(String(255))

        def __init__(self,document, nombre,dni,rol):
                self.document=document
                self.nombre=nombre
                self.dni=dni
                self.rol=rol