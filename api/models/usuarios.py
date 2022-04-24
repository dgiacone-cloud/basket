from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey , Numeric, Date, Boolean,DateTime,BigInteger,Text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

 

 

class Usuarios(db.Base):
    __tablename__ = 'usuarios'

    id=Column(Integer, primary_key=True)
    email=Column(String(100),nullable=False)
    nombre=Column(String(100),nullable=False)
    cliente=Column(String(100))
    admin=Column(String(1))
    clave=Column(String(100))
    
    # # Genero el hash para la password
    # def __create_password(self, password):
    #     return generate_password_hash(password)
    
    # # Funcion que verifica el password ingfresado vs el hash
    # def verify_password(self,password):
    #     return check_password_hash(self.password, password)

   
 
    
    