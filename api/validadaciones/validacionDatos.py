from flask import session
from flask import Flask, redirect, url_for
from sqlalchemy import false, true
class ValidarDatos:
    def datoNone (dato):
        if dato == 'None' or dato is None or dato == ''  :
            dato = 'Sin dato'
            
        
        return dato

    def esDatoNone (dato):
       
        if dato == 'None' or dato is None or dato == ''  :
            return 1
        else:
            return 0